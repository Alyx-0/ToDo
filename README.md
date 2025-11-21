# TODO Flask App

A simple ToDo app based on Python Flask and SQLAlchemy.

## Functions
- Add new tasks with deadline
- Delete existing tasks
- Update existing tasks
- Render existing tasks

## Tech Stack
- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML, CSS
- **DataBase:** SQLite

## DataBase Models
- Tasks
    * id - Primary Key (Int)
    * task - Task Title (String)
    * Deadline - Task Deadline (DateTime)
    * Date - Creation Date (Date)

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
|/|GET|Home Page|
|/planner|GET|Planner Page|
|/add|POST|Add new Task|
|/delete/<int:id>|GET|Delete Task|
|/update-page|GET|Update Page|
|/update/<int:id>|POST|Update Task|

## Requirements
- Flask==3.1.2
- Flask-SQLAlchemy==3.1.1

## Author
GitHub: @Alyx-0