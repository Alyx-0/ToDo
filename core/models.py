from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), unique = False, nullable = False)
    deadline = db.Column(db.DateTime, unique = False, nullable = False)
    date = db.Column(db.Date, unique = False, nullable = False)
