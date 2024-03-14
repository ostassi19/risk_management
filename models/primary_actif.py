from . import db

class PrimaryActif(db.Model):
    __tablename__ = 'primary_actif'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(30), nullable=True)
    description = db.Column(db.Text, nullable=True)
    complementary_description = db.Column(db.Text, nullable=True)
    actif_type = db.Column(db.Text, nullable=True)
    impact_level = db.Column(db.String(1), nullable= True)

    # One-to-Many relationship with PrimaryActif
    risks = db.relationship('Risk', backref='primary_actif', lazy=True)
