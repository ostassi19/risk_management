from enum import Enum
from . import db,user_risk_association
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_security import UserMixin

class UserRoleEnum(Enum):
    MANAGER = 'Risk Manager'
    OWNER = 'Risk Owner'
    RSSI = 'rssi'

class User(db.Model,UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=True, nullable=True)
    last_name = db.Column(db.String(50), unique=True, nullable=True)
    mail = db.Column(db.String(255), unique=True, nullable=True)
    phone = db.Column(db.String(255), unique=True, nullable=True)
    address = db.Column(db.String(255), unique=True, nullable=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    last_use = db.Column(db.Date, nullable=True)
    role = db.Column(db.Enum(UserRoleEnum))

    # Define the relationship to Company
    companies = db.relationship('Company', backref='user', lazy=True)

    risks = db.relationship('Risk', secondary=user_risk_association, back_populates='users')


def hash_password(password):
    """
    It takes the password that the user has entered, hashes it, and then stores the hashed password in
    the database
    """
    password = generate_password_hash(password, rounds=10).decode("utf8")
    return password


def check_password(password1, password2):
    """
    It takes a plaintext password, hashes it, and compares it to the hashed password in the database

    :param password: The password to be hashed
    :return: The password is being returned.
    """
    return check_password_hash(password1, password2)


