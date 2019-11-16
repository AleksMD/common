from flask_restful import Resource
from blueprints.rooms.arg_parser import (room_parser,
                                         room_parser_post,
                                         room_parser_patch)
from blueprints.rooms.room_object_serlzer import marshal_with_decor
from blueprints.rooms.rooms_model import Room
from hotel_db import DB


class Rooms(Resource):
    @marshal_with_decor
    def get(self):
        room_filters = room_parser.parse_args()
        if any(tuple(room_filters.values())):
            return Room.query.filter_by(**room_filters).first()
        return Room.query.all(), 200

    def post(self):
        new_room_values = room_parser_post.parse_args()
        new_room = Room(**new_room_values)
        DB.session.add(new_room)
        DB.session.commit()
        return 'New room was successfully added!', 200

    def patch(self, number):
        room_info_to_update = room_parser_patch.parse_args()
        print(room_info_to_update)
        room_to_update = Room.query.filter_by(number=number).first()
        print(dir(room_to_update))
        if not room_to_update:
            return 'Sorry the room you are looking for was not found.'
        else:
            for key, value in room_info_to_update.items():
                if value:
                    setattr(room_to_update, key, value)
        DB.session.commit()
        return f' Info about room #{room_to_update.number} was successfully updated!', 200

    def delete(self, number):
        room_to_delete = Room.query.filter_by(number=number).first()
        DB.session.delete(room_to_delete)
        DB.session.commit()
        return f'The room #{number} successfully deleted from database!', 200
