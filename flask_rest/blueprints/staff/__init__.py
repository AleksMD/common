from flask_restful import Api
from flask import Blueprint


from blueprints.staff.staff_routes import Staff


staff_page = Blueprint('Staff', __name__)
api = Api(staff_page)
api.add_resource(Staff, '/staff')
