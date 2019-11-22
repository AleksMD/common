from flask_restful import Resource
from flask import request

from blueprints.tenants.arg_parser import (tenant_parser,
                                           tenant_parser_delete)
from blueprints.tenants.tenant_object_serlzer import marshal_with_decor
from blueprints.tenants.tenants_db import tenants_storage, Tenant


class Tenants(Resource):
    @marshal_with_decor
    def get(self):
        tenant_filters = tenant_parser.parse_args()
        response = tenants_storage
        if any(tuple(tenant_filters.values())):
            response = [tenant for tenant in tenants_storage
                        for tenant_filter in tenant_filters.items()
                        if getattr(tenant, tenant_filter[0]) == tenant_filter[1]]
        return response

    def post(self):
        new_tenant_values = request.get_json()
        tenants_storage.append(Tenant(**new_tenant_values))
        return 'New tenant was successfully added!'

    def patch(self):
        tenant_info_to_update = request.get_json()
        tenant_to_update = None
        for tenant in tenants_storage:
            if tenant.name == tenant_info_to_update.get('name'):
                tenant_to_update = tenant
        for key, value in tenant_info_to_update.items():
            setattr(tenant_to_update, key, value)
        return f' Info about tenant - {tenant_to_update.name} was successfully updated!'

    def delete(self):
        tenant_to_delete = tenant_parser_delete.parse_args().get('name')
        for tenant in tenants_storage:
            if tenant.name == tenant_to_delete:
                tenants_storage.remove(tenant)
                return f'The tenant - {tenant.name} successfully deleted from database!'
