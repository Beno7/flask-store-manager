from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser() # initializes a new object which can be used to parse the request
    parser.add_argument('username',
        type=str, # means that this field should be treated as a float e.g., 12.00 will still be 12.00 and not 12 (integer)
        required=True, # means that this field is required
        help="This field cannot be left blank!" # message when value is noneexistent
    )
    parser.add_argument('password',
        type=str, # means that this field should be treated as a float e.g., 12.00 will still be 12.00 and not 12 (integer)
        required=True, # means that this field is required
        help="This field cannot be left blank!" # message when value is noneexistent
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'user already exists'}, 400
        UserModel(**data).save_to_db() # Use kwargs
        return {'message': 'User created successfully.'}, 201
