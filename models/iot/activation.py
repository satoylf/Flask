from models import db

class Activation(db.Model):
    __tablename__ = "activations"
    id = db.Column(db.Integer(), primary_key = True)

