from models import db, User
from datetime import datetime

class Culturas(db.Model):
    __tablename__ = "culturas"
    id = db.Column("id", db.Integer(), primary_key=True)
    user_id = db.Column("user_id", db.Integer(), db.ForeignKey(User.id), nullable=False)
    name = db.Column(db.String(100))
    estacao_ideal = db.Column(db.String(20))
    umidade_ideal = db.Column(db.String(20))
    pressao_ideal = db.Column(db.String(20))
    date_time = db.Column("date_time", db.DateTime(), nullable=False, default=datetime.now())

    area_plantio = db.relationship('Area_plantio', backref='area_plantio')
