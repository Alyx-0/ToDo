from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__, template_folder='./templates', static_folder='./style')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), unique = False, nullable = False)
    deadline = db.Column(db.DateTime, unique = False, nullable = False)
    date = db.Column(db.Date, unique = False, nullable = False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/planner')
def planner():
    tasks = Tasks.query.all()
    return render_template('main.html', tasks=tasks)

@app.route('/add', methods=["POST"])
def add_data():
    task = request.form.get("task")
    deadline = request.form.get("deadline")
    new_task = Tasks(task = task, deadline = datetime.strptime(deadline, '%Y-%m-%dT%H:%M'), date = date.today())
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('planner'))

@app.route('/delete/<int:id>')  
def delete(id):
    data = Tasks.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('planner'))

@app.route('/update-page/<int:id>')
def update_page(id):
    return render_template('update.html', id=id)

@app.route('/update/<int:id>', methods=["POST"])
def update(id): 
    data = Tasks.query.get(id)
    data.task = request.form.get("task")
    data.deadline = datetime.strptime(request.form.get("deadline"), '%Y-%m-%dT%H:%M')
    data.date = date.today()
    db.session.commit()
    return redirect(url_for('planner'))
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)