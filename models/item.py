from db import db

class ItemModel(db.Model): # extends db.Model
    # means that db will make use of this object
    # (similar to mongoose model)
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) # Creates a Foreign Key for Store Reference
    store = db.relationship('StoreModel') # Defines a relationship between StoreModel and this Model

    def __init__(self, name, price, store_id):
        # id will also be passed in, but will not be used (as it is not defined in the set of parameters.)
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        # SELECT * FROM items WHERE name=name LIMIT 1
        # Will convert data to an ItemModel object

    def save_to_db(self): # Performing Upsert
        db.session.add(self)
        db.session.commit()
        # session is collection of objects that can write data to the db
        # Can add multiple objects and perform commit

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
