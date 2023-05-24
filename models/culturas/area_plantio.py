from models import db, Culturas

class Area_plantio(db.Model):
    __tablename__ = "area_plantio"
    id = db.Column(db.Integer, db.ForeignKey(Culturas.id), primary_key=True)
    area = db.Column(db.Float, nullable = False)
