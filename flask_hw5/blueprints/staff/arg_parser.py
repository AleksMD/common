from flask_restful import reqparse

staff_parser = reqparse.RequestParser(bundle_errors=True)
staff_parser.add_argument("name", type=str, location='args')
staff_parser.add_argument("passport_id", type=str, location='args')
staff_parser.add_argument("position", type=str, location='args')
staff_parser.add_argument("salary", type=int, location='args')

staff_parser_post = staff_parser.copy()
staff_parser_post.replace_argument("name",
                                   type=str,
                                   location='form',
                                   required=True,
                                   help='This field cannot be empty.')
staff_parser_post.replace_argument("passport_id",
                                   type=str,
                                   location='form',
                                   required=True,
                                   help='This field cannot be empty.')
staff_parser_post.replace_argument("position",
                                   type=str,
                                   location='form',
                                   required=True,
                                   help='This field cannot be empty.')
staff_parser_post.replace_argument("salary",
                                   type=int,
                                   location='form',
                                   required=True,
                                   help='This field cannot be empty.')

staff_parser_patch = staff_parser.copy()
staff_parser_patch.replace_argument("name",
                                    type=str,
                                    location=['form', 'args'])
staff_parser_patch.replace_argument("passport_id",
                                    type=str,
                                    location=['form', 'args'])
staff_parser_patch.replace_argument("position",
                                    type=str,
                                    location=['form', 'args'])
staff_parser_patch.replace_argument("salary",
                                    type=int,
                                    location=['form', 'args'])

staff_parser_delete = staff_parser.copy()
staff_parser_delete.replace_argument("name",
                                     type=str,
                                     location=['form', 'args'],
                                     required=True,
                                     help='This field cannot be empty.'
                                     )
