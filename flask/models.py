from database import engine, metadata
from sqlalchemy import Table
from sqlalchemy.orm import mapper
from database import metadata, db_session

class User(object):
    query = db_session.query_property()

    def __init__(self, id=None, image=None, email=None,
    	password=None, name=None):
        self.id = id
        self.image = image
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return '<User %r>' % (self.name)

users = Table('_user', metadata, autoload=True)
mapper(User, users)
con = engine.connect()
print (User.query.all())