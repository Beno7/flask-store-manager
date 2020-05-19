from app import app
from db import db

print('running app')

db.init_app(app)

print('db initialized')

@app.before_first_request # before any request, SQLALCHEMY will run this function
def create_tables():
    db.create_all() # Will create all registered dbs (see models)

print('create_tables defined')
