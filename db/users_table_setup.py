import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, create_engine

conn = sqlite3.connect('sqlite:///C:/Users/adamk/Documents/Kursy/Python/AtlasGrzybow/database/users2.sqlite')

# connect to the database
# engine = create_engine('postgresql+psycopg2://tnkzyfat:yX_7g9_Lk-rnrhl2_P2LH6a5-Fk3db3R@tai.db.elephantsql.com/tnkzyfat')
db = SQLAlchemy()


# Users class definition
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))


# function to create table
def create_users_table():
    Users.metadata.create_all(engine)


create_users_table()