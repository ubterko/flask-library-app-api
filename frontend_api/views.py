from frontend_api import app 
from frontend_api.extensions import db
from frontend_api.extensions import login_manager
from frontend_api.models import User, Book

from flask import Flask, jsonify, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

from datetime import datetime, timedelta



login_manager.login_view = 'login'

# login manager
@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

# admin api. returns all users registered on the application
@app.route("/users")
def get_users():
    users = User.query.all()
    data = []
    for user in users:
        data.append({
            "username": user.username,
        })
    return jsonify(data)

# api for registering users
@app.route("/register", methods=['POST'])
def register():
    credentials = request.get_json()
    if credentials:
        db.session.add(
            User(username=credentials.get('username'),
                password=credentials.get('password'))
        )
        db.session.commit()

    return jsonify({"message":"User added successfully"})

# api for getting all available books 
@app.route('/books')
def book():
    all_books = Book.query.filter_by(borrowed=False)
    data = []
    for book in all_books: 
        data.append({
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "publisher": book.publisher
        })
    return jsonify(data)

# api for getting book by id
@app.route('/book/<int:id>')
def get_book_by_id(id):
    book = Book.query.get_or_404(id)
    return jsonify({
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "publisher": book.publisher,
            "user_id": book.user_id,
            "borrowed_date": book.borrowed_date,
            "return_date": book.return_date
        })

# Filter books by publisher or category
# usage: http://localhost:5000/filter_by?category=religion 
# usage: http://localhost:5000/filter_by?publisher=packt
@app.route('/filter_by')
def get_book_by(item):
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

# api for borrowing particular book by id
@app.route("/book/borrow_book/<int:id>")
def borrow_book(id):
    user_id = current_user.id
    book = Book.query.get_or_404(id)
    book.user_id = user_id
    book.borrowed_date = datetime.now()
    # books are returned in 14 days
    book.return_date = datetime.now() + timedelta(14)
    db.session.commit()
    return ({"message": "Successfully borrowed book!"})

# api for getting users and the books they borrowed
@app.route("/get_users_books")
def get_users_books():
    users = User.query.all()
    data = []
    for user in users:
        dict = {'username': user.username, 'books': []}
        for book in user.book:
            dict['books'].append(book.title)
        data.append(dict)
    return jsonify(data)

# api for admin service. lists books that are not available
# and when they will be available
@app.route("/get_unnavailable")
def get_borrowed_books():
    books = Book.query.filter_by(borrowed=True)
    data = []
    for book in books:
        data.append({
            "title": book.title,
            "author": book.author,
            "available date": book.return_date
        })        
    return jsonify(data)
