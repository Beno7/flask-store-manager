from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser() # initializes a new object which can be used to parse the request
    parser.add_argument('price',
        type=float, # means that this field should be treated as a float e.g., 12.00 will still be 12.00 and not 12 (integer)
        required=True, # means that this field is required
        help="This field cannot be left blank!" # message when value is noneexistent
    )
    parser.add_argument('store_id',
        type=int, # means that this field should be treated as a float e.g., 12.00 will still be 12.00 and not 12 (integer)
        required=True, # means that this field is required
        help="Every item needs a store id." # message when value is noneexistent
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': "Item not found."}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name \'{}\' already exists.'.format(name)}, 400
        data = Item.parser.parse_args()
        new_item = ItemModel(name, **data)
        try:
            new_item.save_to_db()
        except:
            return {'message': 'An error occurred.'}, 500
        return new_item.json(), 201 # Return 201 status code. 202 is Accepted, but the creation itself is delayed.

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return { 'items': [x.json() for x in ItemModel.query.all()] } # Will get all data in database
        # return { 'items': list(map(lambda x: x.json(), ItemModel.query.all())) }
