from flask_restful import reqparse

staff_parser = reqparse.RequestParser(bundle_errors=True)
staff_parser.add_argument("name",
                          type=str, location=['form', 'args', 'json'])
staff_parser.add_argument("passport_id",
                          type=str, location=['form', 'args', 'json'])
staff_parser.add_argument("position",
                          type=str, location=['form', 'args', 'json'])
staff_parser.add_argument("salary",
                          type=int, location=['form', 'args', 'json'])

staff_parser_post = staff_parser.copy()
staff_parser_post.replace_argument("name",
                                   type=str,
                                   location=['form', 'args', 'json'],
                                   required=True,
                                   help="This field cannot be empty.")
staff_parser_post.replace_argument("passport_id",
                                   type=str,
                                   location=['form', 'args', 'json'],
                                   required=True,
                                   help='This field cannot be empty.')
staff_parser_post.replace_argument("position",
                                   type=str,
                                   location=['form', 'args', 'json'],
                                   required=True,
                                   help='This field cannot be empty.')
staff_parser_post.replace_argument("salary",
                                   type=int,
                                   location=['form', 'args', 'json'],
                                   required=True,
                                   help='This field cannot be empty.')

staff_parser_patch = staff_parser.copy()
staff_parser_patch.replace_argument("name",
                                    type=str,
                                    location=['form', 'args', 'json'])
staff_parser_patch.replace_argument("passport_id",
                                    type=str,
                                    location=['form', 'args', 'json'])
staff_parser_patch.replace_argument("position",
                                    type=str,
                                    location=['form', 'args', 'json'])
staff_parser_patch.replace_argument("salary",
                                    type=int,
                                    location=['form', 'args', 'json'])

staff_parser_delete = staff_parser.copy()
staff_parser_delete.replace_argument("name",
                                     type=str,
                                     location=['form', 'args', 'json'],
                                     required=True,
                                     help='This field cannot be empty.'
                                     )

staff_room_parser = reqparse.RequestParser(bundle_errors=True)
staff_room_parser.add_argument('staff_id', type=str, required=True)
staff_room_parser.add_argument('room_id', type=int)

staff_room_parser_post = staff_room_parser.copy()
staff_parser_post.replace_argument('room_id', type=int, required=True)
