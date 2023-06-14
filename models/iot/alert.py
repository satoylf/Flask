from models import db, Sensor
from datetime import datetime

class Alert(db.Model):
    __tablename__ = "alerts"
    id = db.Column("id", db.Integer(), primary_key=True)
    sensor_id = db.Column(db.Integer(), db.ForeignKey(Sensor.id))
    temperature = db.Column(db.Float(), nullable=False, default=0.0)
    humidity = db.Column(db.Float(), nullable=False, default=0.0)
    pressure = db.Column(db.Float(), nullable=False, default=0.0)
    message = db.Column(db.String(100), nullable=False, default="Alerta!!")
    date_time = db.Column(db.DateTime(), nullable=False, default=datetime.now())
