from admin_api.extensions import db
from datetime import datetime

from flask_login import UserMixin

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    category = db.Column(db.String)
    publisher = db.Column(db.String)

    def __repr__(self):
        return f'<{self.id}: {self.title[:10]}..>'