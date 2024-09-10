from datetime import datetime, timedelta

from frontend_api import app 
from frontend_api.extensions import db
from frontend_api.extensions import login_manager
from frontend_api.models import Book, Borrow, User
from flask import Flask, jsonify, request, redirect, url_for
from flask_login import login_user, login_required, logout_user

login_manager.login_view = 'login'

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/login", methods=['GET','POST'])
def login():
    credentials = request.get_json()
    user = User.query.filter_by(username=credentials.username)
    if user and (user.password == credentials.password):
        login_user(user)
        return jsonify({"message":"Login successful!"})
    else:
        return jsonify({"message":"Invalid username or password"})

@login_required
@app.route("/logout")
def logout():
    logout_user()
    return jsonify({"message":"User logged out"})

@app.route('/')
def index():
    all_books = Book.query.all()
    data = []
    for book in all_books: 
        data.append({
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "publisher": book.publisher
        })
    return jsonify(data)

@app.route('/book/<int:id>')
def get_book_by_id(id):
    book = Book.query.get_or_404(id)
    return jsonify({
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "publisher": book.publisher
        })
    
@app.route('/book')
def get_book_by_publisher():
    publisher = request.args.get("publisher")
    category = request.args.get("category")

    if publisher:
        books = Book.query.filter_by(publisher=publisher)
    elif category:
        books = Book.query.filter_by(category=category)

    data = []
    for book in books:
         data.append({
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "publisher": book.publisher
        })
    return jsonify(data)

@app.route("/borrow_book/<int:id>", methods=['POST'])
def borrow_book(id):
    book = Book.query.get_or_404(id)
    borrowed_date = datetime.now()
    days = request.args.get("days")
    return_date = datetime.now() + timedelta(days)
    
    db.session.add(
        Borrow(borrowed_date=borrowed_date, return_date=return_date, book_id=book.id)
    )
    db.session.commit()
    return ({"message": "Successfully borrowed book!"})
