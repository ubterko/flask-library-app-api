from celery import Celery

from frontend_api.models import Book as book_frontend_tb
from frontend_api.extensions import db

import celery_config

# app = Celery('bookstore', broker='redis://localhost:6379/0',
#              backend='redis://localhost:6379/0') 

app = Celery('bookstore')
app.config_from_object(celery_config)

@app.task
def update_bookstore(payload):
    for book in payload:
        db.session.add(
            book_frontend_tb(
                title=payload.get("title"),
                author=payload.get("author"),
                category=payload.get("category"),
                publisher=payload.get("publisher")
            )
        )
    return 'Database up to date.'