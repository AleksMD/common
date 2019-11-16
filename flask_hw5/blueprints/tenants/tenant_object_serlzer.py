from flask_restful import marshal_with, fields
from blueprints.rooms.room_object_serlzer import room_structure

tenant_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "gender": fields.String,
    "age": fields.Integer,
    "city": fields.String,
    "address": fields.String,
    "rooms": fields.Nested(room_structure)
}

marshal_with_decor = marshal_with(tenant_structure)
