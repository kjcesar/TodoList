from datetime import datetime
from flask import render_template
from task import Task

## My Imports
from app import app
from forms import TaskForm

current_year = datetime.now().year

tasks = []
"""
    Include Flatpickr JavaScript and CSS files in your Flask template.
    Create datepicker input elements in your HTML template.
    Write JavaScript code to initialize Flatpickr datepicker widgets.
    Serve your Flask application and navigate to the page with the datepicker inputs.
    Access selected dates in your Flask routes and process them as needed.
"""


@app.context_processor
def inject_current_year():
    return dict(current_year=current_year)


@app.route("/", methods=["GET", "POST"])
def home():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(form.task.data)
        tasks.append(new_task)

    return render_template("index.html", form=form, tasks=tasks)
