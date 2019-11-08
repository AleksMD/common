from flask_restful import marshal_with, fields


staff_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "position": fields.String,
    "salary": fields.Integer
}

marshal_with_decor = marshal_with(staff_structure)
