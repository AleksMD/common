from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from blueprints.rooms.room_arg_parser import (room_parser,
                                              room_parser_post,
                                              room_parser_patch)
from blueprints.rooms.room_object_serlzer import marshal_with_decor
from blueprints.rooms.rooms_model import Room
from hotel_db import db


class Rooms(Resource):
    @marshal_with_decor
    def get(self):
        room_filters = room_parser.parse_args()
        if any(tuple(room_filters.values())):
            return Room.query.filter_by(**{k: v
                                           for k, v in room_filters.items()
                                           if v}).first_or_404()
        return Room.query.all(), 200

    @marshal_with_decor
    def post(self):
        new_room_values = room_parser_post.parse_args()
        room_to_add = Room(**new_room_values)
        db.session.add(room_to_add)
        try:
            db.session.commit()
        except SQLAlchemyError:
            return 'Something wrong happened on our side. Please, try later!'
        return room_to_add, 201

    def patch(self, number):
        room_info_to_update = room_parser_patch.parse_args()
        room_to_update = Room.query.filter_by(number=number).first_or_404()
        for key, value in room_info_to_update.items():
            if value:
                setattr(room_to_update, key, value)
        try:
            db.session.commit()
        except SQLAlchemyError:
            return 'Something wrong happened on our side. Please, try later!'
        return f' Info about room #{room_to_update.number} ' \
               f'was successfully updated!', 200

    def delete(self, number):
        room_to_delete = Room.query.filter_by(number=number).first_or_404()
        db.session.delete(room_to_delete)
        try:
            db.session.commit()
        except SQLAlchemyError:
            return 'Something wrong happened on our side. Please, try later!'
        return f'The room #{number} successfully deleted from database!', 204
