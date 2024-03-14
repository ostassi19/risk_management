from enum import Enum
from sqlalchemy import ForeignKey
from . import db


class MESURETYPEEnum(Enum):
    DETERRENT = "dissuasive"
    CONTAINMENT = "confinement"
    PREVENTIVE = "préventive"
    PALLIATE = "palliative"


class Mesure(db.Model):
    __tablename__ = 'mesure'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    measure = db.Column(db.Text, nullable=True)
    # One-to-Many relationship with Mesure
    risks = db.relationship('Risk', backref='mesures', lazy=True)
    type = db.Column(db.Enum(MESURETYPEEnum), nullable=True)

    mesure_level_id = db.Column(db.Integer, db.ForeignKey('mesure_level.id'), nullable=True)







