from enum import Enum
from sqlalchemy import ForeignKey
from . import db


class MESURETYPEEnum(Enum):
    DETERRENT = "dissuasive"
    CONTAINMENT = "confinement"
    PREVENTIVE = "préventive"
    PALLIATE = "palliative"


class Measure(db.Model):
    __tablename__ = 'measure'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    measure = db.Column(db.Text, nullable=True)
    # One-to-Many relationship with Measure
    risks = db.relationship('Risk', backref='measures', lazy=True)
    type = db.Column(db.Enum(MESURETYPEEnum), nullable=True)

    measure_level_id = db.Column(db.Integer, db.ForeignKey('measure_level.id'), nullable=True)



