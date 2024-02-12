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

    def __init__(self, security_impact, consequence_type, name, damage_type, comment, selection):
        self.security_impact = security_impact
        self.consequence_type = consequence_type
        self.name = name
        self.damage_type = damage_type
        self.comment = comment
        self.selection = selection

    def serialize(self):
        return {
            'id': self.id,
            'security_impact': self.security_impact,
            'consequence_type': self.consequence_type,
            'name': self.name,
            'damage_type': self.damage_type,
            'comment': self.comment,
            'selection': self.selection
        }
