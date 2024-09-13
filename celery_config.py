from celery import Celery
from frontend_api.models import Book
from frontend_api.extensions import db

app = Celery('bookstore', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

@app.task
def update_bookstore(payload):
    for book in payload:
        db.session.add(
            Book(
                title=payload.get("title"),
                author=payload.get("author"),
                category=payload.get("category"),
                publisher=payload.get("publisher")
            )
        )
    return 'Database up to date.'