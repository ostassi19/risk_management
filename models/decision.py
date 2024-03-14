from . import db


class Decision(db.Model):
    __tablename__ = 'decision'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    decision_result = db.Column(db.Text, nullable=True)

    # One-to-Many relationship with PrimaryActif
    risks = db.relationship('Risk', backref='decision', lazy=True)

