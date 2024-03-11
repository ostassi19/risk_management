from . import db

class MesureLevel(db.Model):
    __tablename__ = 'mesure_level'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    definition = db.Column(db.Text, nullable=True)

    # One-to-Many relationship with Mesure
    risks = db.relationship('Mesure', backref='mesure_level', lazy=True)