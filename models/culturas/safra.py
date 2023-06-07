from models import db, Culturas
from datetime import datetime

class Safra(db.Model):
    __tablename__ = "safra"
    id = db.Column("id", db.Integer(), db.ForeignKey(Culturas.id), primary_key = True)
    data_plantio = db.Column("data_plantio", db.DateTime(), nullable=False, default=datetime.now())
    date_colheita = db.Column("data_colheita", db.DateTime(), nullable=True)
    producao = db.Column(db.Integer(), nullable=True)

    culturas = db.relationship('Culturas',backref='cultura')