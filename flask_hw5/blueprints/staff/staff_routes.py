from flask_restful import Resource

from blueprints.staff.arg_parser import (staff_parser,
                                         staff_parser_patch,
                                         staff_parser_delete,
                                         staff_parser_post)
from blueprints.staff.staff_db import staff_storage, StaffObj

from blueprints.staff.staff_object_serlzer import marshal_with_decor


class Staff(Resource):
    @marshal_with_decor
    def get(self):
        staff_filters = staff_parser.parse_args()
        response = staff_storage
        if any(tuple(staff_filters.values())):
            response = [staff for staff in staff_storage
                        for staff_filter in staff_filters.items()
                        if getattr(staff, staff_filter[0]) == staff_filter[1]]
        return response

    def post(self):
        new_staff_values = staff_parser_post.parse_args()
        staff_storage.append(StaffObj(**new_staff_values))
        return 'New staff was successfully added!'

    def patch(self):
        staff_info_to_update = staff_parser_patch.parse_args()
        staff_to_update = None
        for staff in staff_storage:
            if staff.name == staff_info_to_update.get('name'):
                staff_to_update = staff
        for key, value in staff_info_to_update.items():
            setattr(staff_to_update, key, value)
        return (f'Info about Staff: {staff_to_update.name}, '
                f'passport #{staff_to_update.passport_id} was successfully updated!')

    def delete(self):
        staff_to_delete = staff_parser_delete.parse_args().get('name')
        for staff in staff_storage:
            if staff.name == staff_to_delete:
                staff_storage.remove(staff)
                return f'The staff - {staff.name} successfully deleted from database!'
