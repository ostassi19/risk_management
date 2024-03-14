from . import db

class SupportActif(db.Model):
    __tablename__ = 'support_actif'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=True)
    type = db.Column(db.Text, nullable=True)
    element = db.Column(db.Text, nullable=True)
    selection = db.Column(db.Boolean, nullable=True)

    # One-to-Many relationship with SupportActif
    risks = db.relationship('Risk', backref='support_actif', lazy=True)
