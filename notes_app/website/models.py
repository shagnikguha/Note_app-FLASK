from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Setting up a one to many relation
class Note(db.Model):
    # Data for each note
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    '''
    Foreign Key --> We must pass a valid ID of an existing user to this field.
    One user can have many notes. 
    The foreign key links one user to the data that is being created at the notes/other data.
    '''
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Can say that this is a child object of User. Note: in SQL all characters are taken in small

class User(db.Model, UserMixin):
    # Data for each user
    id = db.Column(db.Integer, primary_key=True)      # Primary Key --> Unique identifier 
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Setting up relationship with the subclass
    notes = db.relationship('Note')                   # One-to-many realtion
    '''
    note = db.relationship('Note', uselist=False)
    Using this will create a one-to-one correspondance.
    If we remove the user_id column in the Notes funcion, this will then create a many-to-one relation
    '''
    # Essentially tells flask and SQL to add to notes whenever a new note is created.
    # Adds any new note into the notes field