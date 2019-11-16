from hotel_db import DB


class Room(DB.Model):

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    number = DB.Column(DB.Integer, unique=True)
    level = DB.Column(DB.String(100))
    price = DB.Column(DB.Integer)
    status = DB.Column(DB.String(50))




