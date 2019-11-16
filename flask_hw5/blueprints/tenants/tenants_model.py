from hotel_db import DB


class Tenant(DB.Model):

    passport_id = DB.Column(DB.String, unique=True, primary_key=True)
    name = DB.Column(DB.String, unique=True)
    age = DB.Column(DB.Integer)
    gender = DB.Column(DB.String(5))
    city = DB.Column(DB.String)
    address = DB.Column(DB.String)
