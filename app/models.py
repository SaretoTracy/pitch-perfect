from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# a model to define our user data.


# connect our class to our database and allow communication.

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(20))
    firstname = db.Column(db.String(20))
    pitches = db.relationship('Pitch', backref='owner')
    comments = db.relationship('Comment', backref='owner')

    def __repr__(self):
        return f"User('{self.username}')"


class Pitch(db.Model):
    '''
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(), index=True)
    title = db.Column(db.String())
    category = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f'Pitch {self.description}'


class Comment(db.Model):
    '''
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(255), index=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f'Comment {self.content}'
