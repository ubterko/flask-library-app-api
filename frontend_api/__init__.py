from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy 
from frontend_api.extensions import db
from frontend_api.extensions import login_manager
# from frontend_api.models import Book
from config import Config

app = Flask(__name__)
app.config.from_object('config.Config')


# extensions
db.init_app(app)
login_manager.init_app(app)
# login_manager.login_view= 'login'

from . import views

if '__name__' == '__main__':
    app.run(port=5003)
# def create_app(class_config=Config):
#     app = Flask(__name__)
#     app.config.from_object(class_config)

#     #extensions
#     db.init_app(app)

#     #blueprints

#     @app.route('/')
#     def index():
#         all_books = Book.query.all()
#         data = []
#         for book in all_books: 
#             data.append({
#                 "title": book.title,
#                 "author": book.author,
#                 "category": book.category,
#                 "publisher": book.publisher
#             })
#         print(data)
#         return ''
    
#     @app.route('/book/<int:id>')
#     def get_book_by_id(id):
#         book = Book.query.get_or_404(id)
#         return jsonify({"book":book.title})
    
    # @app.route('/book')
    # def get_book_by_publisher():
    #     publisher = request.args(publisher)
    #     return jsonify({"pub": publisher})
    # return app