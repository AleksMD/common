from flask_restful import marshal_with, fields


room_structure = {
    "number": fields.Integer,
    "level": fields.String,
    "price": fields.Integer,
    "status": fields.String,
    "tenant_id": fields.String
}

marshal_with_decor = marshal_with(room_structure)
