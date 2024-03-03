from . import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_security import UserMixin


class User(db.Model,UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    last_use = db.Column(db.Date, nullable=True)


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


