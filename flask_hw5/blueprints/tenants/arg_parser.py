from flask_restful import reqparse

tenant_parser = reqparse.RequestParser(bundle_errors=True)
tenant_parser.add_argument("id", type=int, location=['form', 'args', 'json'])
tenant_parser.add_argument("name", type=str, location=['form', 'args', 'json'])
tenant_parser.add_argument("passport_id", type=str, location=['form', 'args', 'json'])
tenant_parser.add_argument("age", type=int, location=['form', 'args', 'json'])
tenant_parser.add_argument("gender", type=str, location=['form', 'args', 'json'])
tenant_parser.add_argument("room_number", type=int, location=['form', 'args', 'json'])
tenant_parser.add_argument("address", type=dict, location=['form', 'args', 'json'])

tenant_parser_post = tenant_parser.copy()
tenant_parser_post.replace_argument("name",
                                    type=str,
                                    location=['form', 'json'],
                                    required=True,
                                    help='This field cannot be empty.')
tenant_parser_post.replace_argument("passport_id",
                                    type=str,
                                    location=['form', 'json'],
                                    required=True,
                                    help='This field cannot be empty.')
tenant_parser_post.replace_argument("age",
                                    type=int,
                                    location=['form', 'json'],
                                    required=True,
                                    help='This field cannot be empty.')
tenant_parser_post.replace_argument("gender",
                                    type=str,
                                    location=['form', 'json'],
                                    required=True,
                                    help='This field cannot be empty.')
tenant_parser_post.replace_argument("room_number",
                                    type=int,
                                    location=['form', 'json'],
                                    required=True,
                                    help='This field cannot be empty.'
                                    )
tenant_parser_post.replace_argument("address",
                                    type=str,
                                    location=['form', 'json'],
                                    required=True,
                                    help='This field cannot be empty.'
                                    )

tenant_parser_patch = tenant_parser.copy()
tenant_parser_patch.replace_argument("name",
                                     type=str,
                                     location=['form', 'args', 'json'])
tenant_parser_patch.replace_argument("passport_id",
                                     type=str,
                                     location=['form', 'args', 'json'])
tenant_parser_patch.replace_argument("age",
                                     type=int,
                                     location=['form', 'args', 'json'])
tenant_parser_patch.replace_argument("gender",
                                     type=str,
                                     location=['form', 'args', 'json'])
tenant_parser_patch.replace_argument("room_number",
                                     type=int,
                                     location=['form', 'args', 'json'])
tenant_parser_patch.replace_argument("address",
                                     type=str,
                                     location=['form', 'args', 'json'])

tenant_parser_delete = tenant_parser.copy()
tenant_parser_delete.replace_argument("name",
                                      type=str,
                                      location=['form', 'args', 'json'],
                                      required=True,
                                      help='This field cannot be empty.'
                                      )
