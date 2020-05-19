import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') # Use sqlite as default
# Defines where the db resides (in this case, it is sqlite)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Turns off Flask SQLALCHEMY Modification Tracker, not the underlying SQLAlchemy Modification Tracker
app.secret_key = 'secret_key'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db # import here to avoid circular dependency
    db.init_app(app)
    app.run(port=5000, debug=True) # Will provide an html page which will tell what's wrong with the request (for debugging purposes)
