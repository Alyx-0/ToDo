from flask import Blueprint, render_template, redirect, url_for
from .models import Tasks
from .add import add_data
from .delete import delete
from .update import update

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return render_template('home.html')

@api.route('/planner')
def planner():
    tasks = Tasks.query.all()
    return render_template('main.html', tasks=tasks)

@api.route('/add', methods=["POST"])
def routes_add_data():
    add_data()
    return redirect(url_for('api.planner'))   

@api.route('/delete/<int:id>')  
def route_delete(id):
    delete(id)
    return redirect(url_for('api.planner'))

@api.route('/update-page/<int:id>')
def update_page(id):
    return render_template('update.html', id=id)

@api.route('/update/<int:id>', methods=["POST"])
def route_update(id): 
    update(id)
    return redirect(url_for('api.planner'))