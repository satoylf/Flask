from flask_mqtt import Mqtt

mqtt_client = Mqtt()
topic_subscribe = ["Farmville-status", "Farmville-warnings"] #, "Farmville-control"]
