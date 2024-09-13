from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy 
from frontend_api.extensions import db
from frontend_api.extensions import login_manager
from config import FrontendConfig

app = Flask(__name__)
app.config.from_object('config.FrontendConfig')

# extensions
db.init_app(app)
login_manager.init_app(app)

from . import views