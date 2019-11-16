from flask_restful import Resource, Api
from flask import Blueprint
from hotel_db import db

create_tables = Blueprint('create_tables', __name__)


class CreateTables(Resource):
    def get(self):
        db.create_all()
        return 'Table model successfully created'


api = Api(create_tables)
api.add_resource(CreateTables, '/create_tables')
