from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from blueprints.staff.staff_arg_parser import (staff_parser,
                                               staff_parser_patch,
                                               staff_parser_post,
                                               staff_room_parser)
from blueprints.staff.staff_model import StaffObj
from blueprints.rooms.rooms_model import Room
from blueprints.staff.staff_object_serlzer import (marshal_with_decor,
                                                   marshal_with_room_decor)
from hotel_db import db


class Staff(Resource):
    @marshal_with_decor
    def get(self):
        staff_filters = staff_parser.parse_args()
        if any(tuple(staff_filters.values())):
            return StaffObj.query.filter_by(**{k: v
                                               for k, v in staff_filters.items()
                                               if v}).first_or_404()
        return StaffObj.query.all()

    def post(self):
        new_staff_values = staff_parser_post.parse_args()
        db.session.add(StaffObj(**new_staff_values))
        try:
            db.session.commit()
        except SQLAlchemyError:
            return 'Something wrong happened on our side. Please, try later!'
        return 'New staff was successfully added!'

    def patch(self, passport_id=None):
        staff_info_to_update = staff_parser_patch.parse_args()
        staff_to_update = StaffObj.query.filter_by(
                             passport_id=passport_id
                          ).first_or_404()
        for key, value in staff_info_to_update.items():
            if value:
                setattr(staff_to_update, key, value)
        try:
            db.session.commit()
        except SQLAlchemyError:
            return 'Something wrong happened on our side. Please, try later!'
        return (f'Info about Staff: {staff_to_update.name}, '
                f'passport #{staff_to_update.passport_id} '
                f'was successfully updated!')

    def delete(self, passport_id=None):
        staff_to_delete = StaffObj.query.filter_by(
                               passport_id=passport_id
                          ).first_or_404()
        name = staff_to_delete.name
        db.session.delete(staff_to_delete)
        try:
            db.session.commit()
        except SQLAlchemyError:
            return 'Something wrong happened on our side. Please, try later!'
        return f'The staff - {name} successfully deleted from database!'


class StaffRooms(Resource):
    @marshal_with_room_decor
    def get(self):
        filters = staff_room_parser.parse_args(strict=True)
        staff_with_rooms = StaffObj.query.filter_by(
                                    passport_id=filters.get('staff_id')
                           ).first_or_404()
        return staff_with_rooms.rooms

    def post(self):
        data = staff_room_parser.parse_args()
        staff = StaffObj.query.filter_by(passport_id=data.get('staff_id')
                                         ).first_or_404()
        room = Room.query.filter_by(number=data.get('room_id')).first_or_404()
        staff.rooms.append(room)
        try:
            db.session.commit()
        except SQLAlchemyError:
            return 'Something wrong happened on our side. Please, try later!'
        return f'Successfully added the room #{room.number} ' \
               f'to the staff: {staff.passport_id}'
