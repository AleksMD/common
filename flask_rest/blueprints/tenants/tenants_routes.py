from flask_restful import Resource

from blueprints.staff.arg_parser import room_parser, room_parser_post, room_parser_patch, room_parser_delete
from blueprints.rooms.room_object_serlzer import marshal_with_decor
from blueprints.rooms.rooms_db import rooms_storage, Room


class Rooms(Resource):
    @marshal_with_decor
    def get(self):
        room_filters = room_parser.parse_args()
        response = rooms_storage
        if any(tuple(room_filters.values())):
            response = [room for room in rooms_storage
                        for room_filter in room_filters.items()
                        if getattr(room, room_filter[0]) == room_filter[1]]
        return response

    def post(self):
        new_room_values = room_parser_post.parse_args()
        rooms_storage.append(Room(**new_room_values))
        return 'New room was successfully added!'

    def patch(self):
        room_info_to_update = room_parser_patch.parse_args()
        room_to_update = None
        for room in rooms_storage:
            if room.number == room_info_to_update.get('number'):
                room_to_update = room
        for key, value in room_info_to_update.items():
            setattr(room_to_update, key, value)
        return f' Info about room #{room_to_update.number} was successfully updated!'

    def delete(self):
        room_to_delete = room_parser_delete.parse_args().get('number')
        for room in rooms_storage:
            if room.number == room_to_delete:
                rooms_storage.remove(room)
                return f'The room #{room.number} successfully deleted from database!'




