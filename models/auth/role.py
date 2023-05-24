from models.db import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column('id', db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(512))

    users = db.relationship("User", back_populates="roles", secondary="user_roles")