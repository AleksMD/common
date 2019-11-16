from hotel_db import DB


class Room(DB.Model):

    number = DB.Column(DB.Integer, primary_key=True, unique=True)
    level = DB.Column(DB.String(100))
    price = DB.Column(DB.Integer)
    status = DB.Column(DB.String(50))




