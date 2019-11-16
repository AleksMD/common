from hotel_db import db


class Tenant(db.Model):

    passport_id = db.Column(db.String, unique=True, primary_key=True)
    name = db.Column(db.String, unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(5))
    city = db.Column(db.String)
    address = db.Column(db.String)
    rooms = db.relationship('Room', backref='tenant', lazy=True)
