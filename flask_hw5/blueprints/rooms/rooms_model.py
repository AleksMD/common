from hotel_db import db


class Room(db.Model):

    number = db.Column(db.Integer, primary_key=True, unique=True)
    level = db.Column(db.String(100))
    price = db.Column(db.Integer)
    status = db.Column(db.String(50))
    tenant_id = db.Column(db.String, db.ForeignKey('tenant.passport_id'),
                          nullable=False)
