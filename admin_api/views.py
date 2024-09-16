from flask import Flask, request, jsonify
from tasks import update_bookstore
from admin_api import app
from admin_api.extensions import db 
from admin_api.models import Book

import requests

# api for adding books to the database 
@app.route("/add_books", methods=['POST'])
def add_books():
    credentials = request.get_json()
    # celery for async process to update frontend api
    update_bookstore(credentials)
    no_of_books = len(credentials)
    for item in credentials:
        db.session.add(
            Book(
                title=item.get("title"),
                author=item.get("author"),
                category=item.get("category"),
                publisher=item.get("publisher")
            )
        )
        db.session.commit()
    return {"message": f"Successfully added book {no_of_books}"}

# delete a book 
@app.route("/delete_book/<int:book_id>")
def remove_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.query(Book).filter_by(id=book_id).delete()
    db.session.commit()
    return {"message": f"{book.title} has been deleted."} 


# get all users 
@app.route("/get_users")
def get_borrowers_and_book():
    url = "http://localhost:5000/users" 
    response = requests.get(url)
    response = response.json()
    data = []
    for item in response:
        data.append({
            "title": item.get("title"),
            "author": item.get("author"),
            "category": item.get("category"),
            "publisher": item.get("publisher"),
            "user_id": item.get("user_id"),
            "borrowed_date": item.get("borrowed_date"),
            "return_date": item.get("return_date")
        })

# fetches users and the books they have borrowed 
@app.route("/get_borrowers")
def get_users():
    url = "http://localhost:5000/get_users_books"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

# api for retrieving books that are not available for borrowing
@app.route("/get_borrowed_books")
def get_borrowed_books():
    url = "http://localhost:5000/get_unnavailable"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)
