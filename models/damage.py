from . import db

class Damage(db.Model):
    __tablename__ = 'damage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    security_impact = db.Column(db.String(255), nullable=True)
    consequence_type = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=True)
    damage_type = db.Column(db.Text, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    selection = db.Column(db.Boolean, nullable=True)

    # One-to-Many relationship with Damage
    risks = db.relationship('Risk', backref='damage', lazy=True)

