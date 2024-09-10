from frontend_api.extensions import db
from datetime import datetime

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    category = db.Column(db.String)
    publisher = db.Column(db.String)

    def __repr__(self):
        return f'<{self.id}: {self.title[:10]}..>'

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrowed_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __repr__(self):
        return f'<Borrowed: {self.book}>'
    
