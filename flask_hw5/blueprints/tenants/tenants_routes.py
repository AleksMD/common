from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from blueprints.tenants.tenant_arg_parser import (tenant_parser,
                                                  tenant_parser_post,
                                                  tenant_parser_patch)
from blueprints.tenants.tenant_object_serlzer import marshal_with_decor
from blueprints.tenants.tenants_model import Tenant
from hotel_db import db


class Tenants(Resource):
    @marshal_with_decor
    def get(self):
        tenant_filters = tenant_parser.parse_args()
        if any(tuple(tenant_filters.values())):
            return Tenant.query.filter_by(**{k: v
                                            for k, v in tenant_filters.items()
                                            if v}).first_or_404()
        return Tenant.query.all(), 200

    @marshal_with_decor
    def post(self):
        new_tenant_values = tenant_parser_post.parse_args()
        tenant_to_add = Tenant(**new_tenant_values)
        db.session.add(tenant_to_add)
        try:
            db.session.commit()
        except SQLAlchemyError:
            return 'Something wrong happened on our side. Please, try later!'
        return tenant_to_add, 201

    def patch(self, passport_id=None):
        tenant_info_to_update = tenant_parser_patch.parse_args()
        tenant_to_update = Tenant.query.filter_by(
                                        passport_id=passport_id
                                        ).first_or_404()
        for key, value in tenant_info_to_update.items():
            if value:
                setattr(tenant_to_update, key, value)
        try:
            db.session.commit()
        except SQLAlchemyError:
            return 'Something wrong happened on our side. Please, try later!'
        return f' Info about tenant - {tenant_to_update.name} ' \
               f'was successfully updated!', 200

    def delete(self, passport_id=None):
        tenant_to_delete = Tenant.query.filter_by(
                                        passport_id=passport_id
                                            ).first_or_404()
        name = tenant_to_delete.name
        db.session.delete(tenant_to_delete)
        try:
            db.session.commit()
        except SQLAlchemyError:
            return 'Something wrong happened on our side. Please, try later!'
        return f'The tenant - {name} successfully deleted from database!', 204
