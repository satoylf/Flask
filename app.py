from flask import Flask, render_template, session, g
from controllers.base_controller import base
from controllers.auth_controller import auth
from controllers.iot_controller import iot
from controllers.login_controller import login
from controllers.cadastro_controller import cadastro

app = Flask(__name__, template_folder="./views/", static_folder="./static/")

app.register_blueprint(base, url_prefix='/base')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(iot, url_prefix='/iot')
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(cadastro, url_prefix='/cadastro')

@app.route('/')
def index():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)