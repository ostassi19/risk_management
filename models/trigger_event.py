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
    selected = db.Column(db.Boolean, nullable=True)

    risks = db.relationship('Risk', backref='trigger_event', lazy=True)

    def __init__(self, code_type, type, code, event, standard_natural_exposure, decision_natural_exposure,
                 result_natural_exposure, comment, selected):
        self.code_type = code_type
        self.type = type
        self.code = code
        self.event = event
        self.standard_natural_exposure = standard_natural_exposure
        self.decision_natural_exposure = decision_natural_exposure
        self.result_natural_exposure = result_natural_exposure
        self.comment = comment
        self.selected = selected

    def serialize(self):
        return {
            'id': self.id,
            'code_type': self.code_type,
            'type': self.type,
            'code': self.code,
            'event': self.event,
            'standard_natural_exposure': self.standard_natural_exposure,
            'decision_natural_exposure': self.decision_natural_exposure,
            'result_natural_exposure': self.result_natural_exposure,
            'comment': self.comment,
            'selected': self.selected
        }