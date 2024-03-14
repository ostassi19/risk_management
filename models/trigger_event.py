from . import db


class TriggerEvent(db.Model):
    __tablename__ = 'trigger_event'
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    code_type = db.Column(db.String(30), nullable= True)
    type = db.Column(db.Text, nullable=True)
    code = db.Column(db.String(30), nullable=True)
    event = db.Column(db.Text, nullable=True)
    standard_natural_exposure = db.Column(db.Integer, nullable=True)
    decision_natural_exposure = db.Column(db.Integer, nullable=True)
    result_natural_exposure = db.Column(db.Integer, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    selection = db.Column(db.Boolean, nullable=True, default=False)
    risks = db.relationship('Risk', backref='trigger_event', lazy=True)

