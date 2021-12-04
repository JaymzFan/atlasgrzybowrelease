import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, create_engine

conn = sqlite3.connect('C:/Users/adamk/Documents/Kursy/Python/AtlasGrzybow/database/users.sqlite')

# connect to the database
engine = create_engine(f'sqlite:///C:/Users/adamk/Documents/Kursy/Python/AtlasGrzybow/database/users.sqlite')
db = SQLAlchemy()


# Users class definition
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))


Users_tbl = Table('users', Users.metadata)


# function to create table
def create_users_table():
    Users.metadata.create_all(engine)


create_users_table()