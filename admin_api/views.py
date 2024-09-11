from flask import Flask, request, jsonify
from admin_api import app
from admin_api.extensions import db 
from admin_api.models import Book

import requests

@app.route("/add_books", methods=['POST'])
def add_books():
    credentials = request.get_json()
    
    for item in credentials:
        db.session.add(
            Book(
                title=credentials.get("title"),
                author=credentials.get("author"),
                category=credentials.get("category"),
                publisher=credentials.get("publisher")
            )
        )
        db.session.commit()
    return {"message": f"Successfully added book {credentials.get('title')}"}

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

@app.route("/get_users")
def get_users():
    url = "http://localhost:5000/get_users_books"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)
