from flask_restful import Api
from flask import Blueprint


from blueprints.rooms.rooms_routes import Rooms


rooms_page = Blueprint('Rooms', __name__)
api = Api(rooms_page)
api.add_resource(Rooms, '/rooms', '/room/<number>')