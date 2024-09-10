from flask import Flask, request, jsonify
from admin_api import app
from admin_api.extensions import db 
from admin_api.models import Book, Borrow

@app.route("/add_books", methods=['POST'])
def add_books():
    credentials = request.get_json()
    
    for item in credentials:
        db.session.add(
            Book(
                title=credentials.title,
                author=credentials.author,
                category=credentials.category,
                publisher=credentials.publisher
            )
        )
    return

@app.route("/books")
def get_books():
    books = Book.query.all()
    data = []
    for book in books:
        data.append({
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "publisher": book.publisher
        })
    return jsonify(data)