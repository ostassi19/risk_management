from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


user_risk_association = db.Table(
    'user_risk_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('risk_id', db.Integer, db.ForeignKey('risk.id'))
)


