from flask_restful import Api
from flask import Blueprint


from blueprints.tenants.tenants_routes import Tenants


tenants_page = Blueprint('Tenants', __name__)
api = Api(tenants_page)
api.add_resource(Tenants, '/tenants')
