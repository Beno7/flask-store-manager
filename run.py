from app import init_app
from db import db

db.init_app(app)

@app.before_first_request # before any request, SQLALCHEMY will run this function
def create_tables():
    db.create_all() # Will create all registered dbs (see models)
