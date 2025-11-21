from .models import db, Tasks
from flask import request
from datetime import datetime, date

def update(id): 
    data = Tasks.query.get(id)
    data.task = request.form.get("task")
    data.deadline = datetime.strptime(request.form.get("deadline"), '%Y-%m-%dT%H:%M')
    data.date = date.today()
    db.session.commit()