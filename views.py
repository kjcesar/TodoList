from datetime import datetime
from flask import render_template, jsonify, url_for, redirect
from task import Task

## My Imports
from app import app, db
from forms import DoneForm, TaskForm
from models import TaskModel

current_year = datetime.now().year


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
    new_task_form = TaskForm()
    tasks_forms = []
    # all_tasks = get_all_tasks().json if get_all_tasks() != "No Tasks" else None

    result = db.session.execute(db.select(TaskModel))
    all_tasks_models = result.scalars().all()
    all_tasks = []
    completed_task = []
    incomplete_task = []
    for model in all_tasks_models:
        task_from_model = Task.from_model(model)
        all_tasks.append(task_from_model)

    print(all_tasks)

    if new_task_form.validate_on_submit() and new_task_form.task.data != None:
        new_task = Task(new_task_form.task.data)
        add_task(new_task)
    # if buttons_form.validate_on_submit():
    #     for task in all_tasks:
    #         if buttons_form.done.data:
    #             task.mark_as_complete()

    for task in all_tasks:
        if task.completed:
            completed_task.append(task)
        else:
            incomplete_task.append(task)

    for task in incomplete_task:
        new_form = DoneForm()
        new_form.done.label.text = task.title
        tasks_forms.append(new_form)

    for form in tasks_forms:
        if form.validate_on_submit():
            if form.complete.data:
                print("task completed")
            elif form.remove.data:  # proccess the form without Checkbox
                print("task deleted")

    return render_template(
        "index.html",
        new_task_form=new_task_form,
        tasks_forms=tasks_forms,
        tasks=all_tasks,
    )


## API
@app.route("/all", methods=["GET"])
def get_all_tasks():
    try:
        result = db.session.execute(db.select(TaskModel))
        all_tasks = result.scalars().all()
        return jsonify(tasks=[task.to_dict() for task in all_tasks])
    except:
        return "No Tasks"


def add_task(task_to_be_added):
    new_task = task_to_be_added.to_model()
    db.session.add(new_task)
    db.session.commit()
