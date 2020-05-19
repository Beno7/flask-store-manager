from db import db

# A helper which allows us to access the data without polluting the Resources
# UserModel is now an API
class UserModel(db.Model): # extends db.Model
    # means that db will make use of this object
    # (similar to mongoose model)
    __tablename___ = 'users' # Required by SQLAlchemy - The Table name
    # Define Columns
    id = db.Column(db.Integer, primary_key=True) # Auto Incrementing
    username = db.Column(db.String(80)) # 80 Characters Maximum
    password = db.Column(db.String(80))

    # The properties should match the column names above
    # So that it gets stored in the Database
    def __init__(self, username, password):
        # No need to define id as SQLAlchemy will define it for us
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
