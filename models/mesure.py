from sqlalchemy import ForeignKey
from . import db

class Mesure(db.Model):
    __tablename__ = 'mesure'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    measure = db.Column(db.Text, nullable=True)
    # One-to-Many relationship with Mesure
    risks = db.relationship('Risk', backref='mesures', lazy=True)

    mesure_level_id = db.Column(db.Integer, db.ForeignKey('mesure_level.id'), nullable=True)


    def __init__(self, measure=None,mesure_level_id= None):
        self.measure = measure
        self.mesure_level_id = mesure_level_id

    def serialize(self):
        return {
            'id': self.id,
            'measure': self.measure,
        }

class Deterrent(Mesure):
    __tablename__ = 'deterrent'
    id = db.Column(db.Integer, db.ForeignKey('mesure.id'), primary_key=True)
    additional_param = db.Column(db.Text, nullable=True)
    __mapper_args__ = {'polymorphic_identity': 'deterrent'}

    def __init__(self, level=None, measure=None, additional_param=None):
        super().__init__(level, measure)
        self.additional_param = additional_param


class Containment(Mesure):
    __tablename__ = 'containment'
    id = db.Column(db.Integer, db.ForeignKey('mesure.id'), primary_key=True)
    another_param = db.Column(db.Text, nullable=True)
    __mapper_args__ = {'polymorphic_identity': 'containment'}

    def __init__(self, level=None, measure=None, another_param=None):
        super().__init__(level, measure)
        self.another_param = another_param


class Preventive(Mesure):
    __tablename__ = 'preventive'
    specific_param = db.Column(db.Text, nullable=True)
    __mapper_args__ = {'polymorphic_identity': 'preventive'}

    def __init__(self, level=None, measure=None, specific_param=None):
        super().__init__(level, measure)
        self.specific_param = specific_param

class Paliale(Mesure):
    __tablename__ = 'paliale'
    custom_param = db.Column(db.Text, nullable=True)
    __mapper_args__ = {'polymorphic_identity': 'paliale'}

    def __init__(self, level=None, measure=None, custom_param=None):
        super().__init__(level, measure)
        self.custom_param = custom_param
