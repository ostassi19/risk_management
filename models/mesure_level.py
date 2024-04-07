from . import db

class MeasureLevel(db.Model):
    __tablename__ = 'measure_level'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    definition = db.Column(db.Text, nullable=True)

    # One-to-Many relationship with Measure
    measures = db.relationship('Measure', backref='measure_level', lazy=True)
