from . import db,user_risk_association



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
    comment = db.Column(db.Text, nullable=True)
    residual_gravity = db.Column(db.Integer, nullable=True)

    # One-to-Many relationship with Measure
    mesures = db.relationship('Measure', backref='risks', lazy=True)

    support_actif_id = db.Column(db.Integer, db.ForeignKey('support_actif.id'), nullable=True)
    damage_id = db.Column(db.Integer, db.ForeignKey('damage.id'), nullable=True)
    primary_actif_id = db.Column(db.Integer, db.ForeignKey('primary_actif.id'), nullable=True)
    trigger_event_id = db.Column(db.Integer, db.ForeignKey('trigger_event.id'), nullable=True)
    decision_id = db.Column(db.Integer, db.ForeignKey('decision.id'), nullable=True)
    users = db.relationship('User', secondary=user_risk_association, back_populates='risks', viewonly=True)

