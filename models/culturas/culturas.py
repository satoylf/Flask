from models import db, User
from datetime import datetime
from sqlalchemy.sql import func

class Culturas(db.Model):
    __tablename__ = "culturas"
    id = db.Column("id", db.Integer(), primary_key=True)
    user_id = db.Column("user_id", db.Integer(), db.ForeignKey(User.id))
    name = db.Column(db.String(100))
    estacao_ideal = db.Column(db.String(20))
    umidade_ideal = db.Column(db.String(20))
    pressao_ideal = db.Column(db.String(20))
    date_time = db.Column("date_time", db.DateTime(), nullable=False, default=datetime.now())

    area_plantio = db.relationship('Area_plantio', backref='area_plantio')

    def save_cultura(name, estacao_ideal, umidade_ideal, pressao_ideal):
        cultura = Culturas(name = name, estacao_ideal = estacao_ideal, \
                umidade_ideal=umidade_ideal, pressao_ideal=pressao_ideal, date_time=func.now())
        db.session.add(cultura)
        db.session.commit()
    
    def get_culturas():
        culturas = Culturas.query.add_columns(Culturas.id, Culturas.name, Culturas.estacao_ideal, \
                            Culturas.umidade_ideal, Culturas.pressao_ideal, Culturas.date_time).all()
        return culturas
    
    def delete_cultura(id):
        try:
            Culturas.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False

    def delete_cultura_by_estacao(estacao_ideal):
        Culturas.query.filter_by(estacao_ideal=estacao_ideal).delete()
        db.session.commit()

    def update_cultura(data):
        Culturas.query.filter_by(id=data['id'])\
                .update(dict(name = data['name'], estacao_ideal = data['estacao_ideal'],\
                             umidade_ideal=data['umidade_ideal'], pressao_ideal=data['pressao_ideal']))
        db.session.commit()
