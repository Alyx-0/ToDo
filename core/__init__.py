from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db
from .routes import api

def run_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../style')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(api)
    return app