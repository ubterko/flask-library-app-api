from flask import Flask, jsonify, request
from admin_api.extensions import db

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

from admin_api import views