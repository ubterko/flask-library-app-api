from datetime import datetime, timedelta

from frontend_api import app 
from frontend_api.extensions import db
from frontend_api.extensions import login_manager
from frontend_api.models import User, Book # Borrow, User
from flask import Flask, jsonify, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

import requests

login_manager.login_view = 'login'

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/users")
def get_users():
    users = User.query.all()
    data = []
    for user in users:
        data.append({
            "username": user.username,
        })
    return jsonify(data)

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


@app.route("/login", methods=['GET','POST'])
def login():
    credentials = request.get_json()
    user = User.query.filter_by(username=credentials.get("username")).first()
    if user and (user.password == credentials.get("password")):
        login_user(user)
        print(user)
        return jsonify({"message":"Login successful!"})
    else:
        return jsonify({"message":"Invalid username or password"})

@login_required
@app.route("/logout")
def logout():
    logout_user()
    return jsonify({"message":"User logged out"})

@app.route('/books')
def book():
    url = 'http://localhost:5003/books'
    load = []
    response = requests.get(url)
    for item in response.json():
        load.append(
            Book(
                title=item.get("title"),
                author=item.get("author"),
                publisher=item.get("publisher"),
                category=item.get("category")
            )
        )
    db.session.add_all(load)
    db.session.commit()

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
            "publisher": book.publisher,
            "user_id": book.user_id,
            "borrowed_date": book.borrowed_date,
            "return_date": book.return_date
        })
    
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

@app.route("/unavailable_books")
def unavailable_books():
    books = Book.query.filter_by(borrowed_date=None)
    data = []
    for book in books:
        data.append({
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "publisher": book.publisher
        })        
    return jsonify(data)
