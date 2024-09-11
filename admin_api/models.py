from admin_api.extensions import db
from datetime import datetime

from flask_login import UserMixin

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    category = db.Column(db.String)
    publisher = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    borrowed_date = db.Column(db.DateTime, nullable=True)
    return_date = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<{self.id}: {self.title[:10]}..>'
    
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    book = db.relationship('Book', backref="user")

    def __repr__(self):
        return f'<{self.id}: {self.username}>'