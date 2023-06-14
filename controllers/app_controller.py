from flask import Flask, render_template, session, g
from controllers.auth_controller import auth
from controllers.admin_controller import admin
from controllers.iot_controller import status, warn
from datetime import datetime
import json

from models.db import db, instance
from models.mqtt import mqtt_client, topic_subscribe
from models import Read, Alert
from flask_login import LoginManager

def create_app() -> Flask:
    app = Flask(__name__, template_folder="./views/",
                        static_folder="./static/",
                        root_path="./")

    app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True
    mqtt_client.init_app(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(admin, url_prefix='/admin')

    @app.route('/')
    def index():
        return render_template("home.html")

    @app.route('/status')
    def get_status():
        return status

    @app.route('/warn')
    def get_warn():
        return warn

    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected successfully')
            for topic in topic_subscribe:
                mqtt_client.subscribe(topic) # subscribe topic
        else:
            print('Bad connection. Code:', rc)

    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        global warn
        data = dict(
            topic=message.topic,
            payload=message.payload.decode()
        )
        print('Received message on topic: {topic} with payload: {payload}'.format(**data))
        if(message.topic in topic_subscribe):
            with app.app_context():
                values = json.loads(data["payload"])
                status['t'] = values['t']
                status['h'] = values['h']
                status['p'] = values['p']
                warn = ""
                reads = Read(date_time=datetime.now(), temperature=values['t'], humidity=values['h'], pressure=values['p'], sensor_id=values['id'])
                db.session.add(reads)
                if message.topic == "Farmville-warnings":
                    warn = values['w']
                    alerts = Alert(date_time=datetime.now(), temperature=values['t'], humidity=values['h'], pressure=values['p'], message=values['w'], sensor_id=values['id'])
                    db.session.add(alerts)
                db.session.commit()

    return app

