from hotel_db import db

anchor_table = db.Table('anchor_table',
                        db.Column('staff_id',
                                  db.String,
                                  db.ForeignKey('staff.passport_id'),
                                  primary_key=True),
                        db.Column('room_id',
                                  db.Integer,
                                  db.ForeignKey('room.number'),
                                  primary_key=True)
                        )


class StaffObj(db.Model):
    __tablename__ = 'staff'
    passport_id = db.Column(db.String, primary_key=True, unique=True)
    name = db.Column(db.String, unique=True)
    position = db.Column(db.String)
    salary = db.Column(db.Integer)
    rooms = db.relationship('Room', secondary=anchor_table, lazy='subquery',
                            backref=db.backref('rooms', lazy=True))
