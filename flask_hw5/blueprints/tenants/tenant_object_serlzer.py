from flask_restful import marshal_with, fields


tenant_address_structure = {
    "city": fields.String,
    "street": fields.String,
    "house_number": fields.Integer
}

tenant_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "room_number": fields.Integer,
    "gender": fields.String,
    "age": fields.Integer,
    "address": fields.Nested(tenant_address_structure)
}

marshal_with_decor = marshal_with(tenant_structure)
