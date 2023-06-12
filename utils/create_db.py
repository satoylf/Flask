from models import *
from flask import Flask

def create_db(app:Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()
        device = Device(name="TEST", brand="TEST", model="TEST",
                        description="TEST", voltage=5.0, is_active=True)

        sensor = Sensor(id=device.id, measure="TEST")

        device.sensors.append(sensor)
        db.session.add(device)
        db.session.commit()
