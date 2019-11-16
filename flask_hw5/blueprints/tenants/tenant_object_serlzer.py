from flask_restful import marshal_with, fields


tenant_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "room_number": fields.Integer,
    "gender": fields.String,
    "age": fields.Integer,
    "city": fields.String,
    "address": fields.String
}

marshal_with_decor = marshal_with(tenant_structure)
