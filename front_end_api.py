from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///frontend_db.sqlite'

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.column(db.String,)
    author = db.Column(db.String)
    category = db.Column(db.String)
    publisher = db.Column(db.String)

