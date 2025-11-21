from .models import db, Tasks

def delete(id):
    data = Tasks.query.get(id)
    db.session.delete(data)
    db.session.commit()