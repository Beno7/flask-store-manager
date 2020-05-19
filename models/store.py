from db import db

class StoreModel(db.Model): # extends db.Model
    # means that db will make use of this object
    # (similar to mongoose model)
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')
    # Defines a relationship between ItemModel and this Model
    # lazy='dynamic' no longer gets a list of items immediately.
    # Now, it is a query builder (instead of a list of ItemModel)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [x.json() for x in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
