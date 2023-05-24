from models import db

class Actuator(db.Model):
    __tablename__ = "actuator"
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(256), nullable = False)