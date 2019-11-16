from flask_restful import Resource
from flask import request

from blueprints.tenants.arg_parser import tenant_parser
from blueprints.tenants.tenant_object_serlzer import marshal_with_decor
from blueprints.tenants.tenants_model import Tenant
from hotel_db import DB


class Tenants(Resource):
    @marshal_with_decor
    def get(self):
        tenant_filters = tenant_parser.parse_args()
        if any(tuple(tenant_filters.values())):
            return Tenant.query.filter_by(**tenant_filters).first(), 200
        return Tenant.query.all(), 200

    def post(self):
        new_tenant_values = request.get_json()
        DB.session.add(Tenant(**new_tenant_values))
        DB.session.commit()
        return 'New tenant was successfully added!', 200

    def patch(self, passport_id):
        tenant_info_to_update = request.get_json()
        tenant_to_update = Tenant.query.filter_by(passport_id=passport_id).first_or_404()
        for key, value in tenant_info_to_update.items():
            setattr(tenant_to_update, key, value)
        DB.session.commit()
        return f' Info about tenant - {tenant_to_update.name} was successfully updated!', 200

    def delete(self, passport_id):
        tenant_to_delete = Tenant.query.filter_by(passport_id=passport_id).first_or_404()
        name = tenant_to_delete.name
        DB.session.delete(tenant_to_delete)
        DB.session.commit()
        return f'The tenant - {name} successfully deleted from database!', 200
