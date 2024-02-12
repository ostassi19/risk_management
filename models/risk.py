from . import db

class Risk(db.Model):
    __tablename__ = 'risk'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    consequence_type = db.Column(db.String(1), nullable=True)
    intrinsic_impact = db.Column(db.Integer, nullable=True)
    personalized_intrinsic_impact = db.Column(db.Integer, nullable=True)
    intrinsic_gravity = db.Column(db.Integer, nullable=True)
    intrinsic_potential = db.Column(db.Integer, nullable=True)
    residual_potential = db.Column(db.Integer, nullable=True)
    personalized_residual_potential = db.Column(db.Integer, nullable=True)
    residual_impact = db.Column(db.Integer, nullable=True)
    decision = db.Column(db.String(255), nullable=True)
    residual_gravity = db.Column(db.Integer, nullable=True)

    mesure_id = db.Column(db.Integer, db.ForeignKey('mesure.id'), nullable=True)

    support_actif_id = db.Column(db.Integer, db.ForeignKey('support_actif.id'), nullable=True)

    damage_id = db.Column(db.Integer, db.ForeignKey('damage.id'), nullable=True)

    primary_actif_id = db.Column(db.Integer, db.ForeignKey('primary_actif.id'), nullable=True)

    trigger_event_id = db.Column(db.Integer, db.ForeignKey('trigger_event.id'), nullable=True)

    def __init__(self, consequence_type, intrinsic_impact, personalized_intrinsic_impact,
                 intrinsic_gravity, intrinsic_potential, residual_potential,
                 personalized_residual_potential, residual_impact, decision, residual_gravity,
                 damage_id,mesure_id,support_actif_id,trigger_event_id):
        self.consequence_type = consequence_type
        self.intrinsic_impact = intrinsic_impact
        self.personalized_intrinsic_impact = personalized_intrinsic_impact
        self.intrinsic_gravity = intrinsic_gravity
        self.intrinsic_potential = intrinsic_potential
        self.residual_potential = residual_potential
        self.personalized_residual_potential = personalized_residual_potential
        self.residual_impact = residual_impact
        self.decision = decision
        self.residual_gravity = residual_gravity
        self.damage_id = damage_id
        self.mesure_id = mesure_id
        self.support_actif_id = support_actif_id
        self.trigger_event_id = trigger_event_id

    def serialize(self):
        return {
            'id': self.id,
            'consequence_type': self.consequence_type,
            'intrinsic_impact': self.intrinsic_impact,
            'personalized_intrinsic_impact': self.personalized_intrinsic_impact,
            'intrinsic_gravity': self.intrinsic_gravity,
            'intrinsic_potential': self.intrinsic_potential,
            'residual_potential': self.residual_potential,
            'personalized_residual_potential': self.personalized_residual_potential,
            'residual_impact': self.residual_impact,
            'decision': self.decision,
            'residual_gravity': self.residual_gravity,
            'mesures': [mesure.serialize() for mesure in self.mesures]
        }
