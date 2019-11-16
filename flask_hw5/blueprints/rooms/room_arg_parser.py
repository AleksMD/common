from flask_restful import reqparse

room_parser = reqparse.RequestParser(bundle_errors=True)
room_parser.add_argument("number", type=int, location=['form', 'args', 'json'])
room_parser.add_argument("price", type=int, location=['form', 'args', 'json'])
room_parser.add_argument("level", type=str, location=['form', 'args', 'json'])
room_parser.add_argument("status", type=str, location=['form', 'args', 'json'])
room_parser.add_argument("tenant_id",
                         type=str, location=['form', 'args', 'json'])

room_parser_post = room_parser.copy()
room_parser_post.replace_argument("number",
                                  type=int,
                                  location=['form', 'args', 'json'],
                                  required=True,
                                  help='This field cannot be empty.')
room_parser_post.replace_argument("price",
                                  type=int,
                                  location=['form', 'args', 'json'],
                                  required=True,
                                  help='This field cannot be empty.')
room_parser_post.replace_argument("level",
                                  type=str,
                                  location=['form', 'args', 'json'],
                                  required=True,
                                  help='This field cannot be empty.')
room_parser_post.replace_argument("status",
                                  type=str,
                                  location=['form', 'args', 'json'],
                                  required=True,
                                  help='This field cannot be empty.')

room_parser_patch = room_parser.copy()
room_parser_patch.replace_argument("number",
                                   type=int,
                                   location=['form', 'args', 'json'])
room_parser_patch.replace_argument("price",
                                   type=int,
                                   location=['form', 'args', 'json'])
room_parser_patch.replace_argument("level",
                                   type=str,
                                   location=['form', 'args', 'json'])
room_parser_patch.replace_argument("status",
                                   type=str,
                                   location=['form', 'args', 'json'])

room_parser_delete = room_parser.copy()
room_parser_delete.replace_argument("number",
                                    type=int,
                                    location=['form', 'args', 'json'],
                                    required=True,
                                    help='This field cannot be empty.'
                                    )
