from models.db import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer(), primary_key=True)
    name = db.Column(db.String(45) , nullable=False, unique=True)
    username = db.Column(db.String(45) , nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(1024) , nullable=False)
    
    roles = db.relationship("Role", back_populates="users", secondary="roles")
    reads = db.relationship("Read", backref="users", lazy=True)