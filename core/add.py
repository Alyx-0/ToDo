from .models import Tasks, db
from flask import request
from datetime import date, datetime

def add_data():
    task = request.form.get("task")
    deadline = request.form.get("deadline")
    new_task = Tasks(task = task, deadline = datetime.strptime(deadline, '%Y-%m-%dT%H:%M'), date = date.today())
    db.session.add(new_task)
    db.session.commit() 