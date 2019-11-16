from flask_restful import marshal_with, fields

from blueprints.rooms.room_object_serlzer import room_structure

staff_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "position": fields.String,
    "salary": fields.Integer,
    "rooms": fields.Nested(room_structure)
}

marshal_with_decor = marshal_with(staff_structure)
marshal_with_room_decor = marshal_with(room_structure)
