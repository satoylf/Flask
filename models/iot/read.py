from models import db, Sensor, User
from datetime import datetime

class Read(db.Model):
    __tablename__ = "reads"
    id = db.Column("id", db.Integer(), primary_key=True)
    sensor_id = db.Column(db.Integer(), db.ForeignKey(Sensor.id), nullable=False)
    temperature = db.Column(db.Float(), nullable=False, default=0.0)
    humidity = db.Column(db.Float(), nullable=False, default=0.0)
    pressure = db.Column(db.Float(), nullable=False, default=0.0)
    date_time = db.Column( db.DateTime(), nullable=False, default=datetime.now())
