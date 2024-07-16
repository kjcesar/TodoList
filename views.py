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
    # all_tasks = get_all_tasks().json if get_all_tasks() != "No Tasks" else None

    result = db.session.execute(db.select(TaskModel))
    all_tasks_models = result.scalars().all()
    all_tasks = []
    completed_tasks = []
    incomplete_tasks = []
    for model in all_tasks_models:
        task_from_model = Task.from_model(model)
        all_tasks.append(task_from_model)

    print(all_tasks[0].task_id)

    if new_task_form.validate_on_submit() and new_task_form.task.data != None:
        new_task = Task(new_task_form.task.data)
        add_task(new_task)
    # if buttons_form.validate_on_submit():
    #     for task in all_tasks:
    #         if buttons_form.done.data:
    #             task.mark_as_complete()

    for task in all_tasks:
        if task.completed:
            completed_tasks.append(task)
        else:
            incomplete_tasks.append(task)

    return render_template(
        "index.html",
        new_task_form=new_task_form,
        incomplete_tasks=incomplete_tasks,
        complete_tasks=completed_tasks
    )

@app.route("/remove_pressed/<int:task_id>", methods=["POST"])
def remove_task(task_id):
    print(f"Remove task no. {task_id}")
    delete_task(task_id)
    return redirect(url_for("home"))

@app.route("/complete_task/<int:task_id>", methods=["POST"])
def mark_complete_task(task_id):
    print(f"Comlete task no. {task_id}")
    task_to_be_completed = db.get_or_404(TaskModel, task_id, description="Task not found")
    if task_to_be_completed:
        task_to_be_completed.completed = True
        db.session.commit()
    return redirect(url_for("home"))

@app.route("/incomplete_task/<int:task_id>", methods=["POST"])
def mark_incomplete_task(task_id):
    print(f"Mark task no. {task_id} as incomplete")
    task_to_be_incompleted = db.get_or_404(TaskModel, task_id, description="Task not found")
    if task_to_be_incompleted:
        task_to_be_incompleted.completed = False
        db.session.commit()
    return redirect(url_for("home"))

## API
@app.route("/all", methods=["GET"])
def get_all_tasks():
    try:
        result = db.session.execute(db.select(TaskModel))
        all_tasks = result.scalars().all()
        return jsonify(tasks=[task.to_dict() for task in all_tasks])
    except:
        return "No Tasks"


# DELETE
@app.route("/remove-task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task_to_be_deleted = db.get_or_404(
        TaskModel, task_id, description="Task not found"
    )
    if task_to_be_deleted:
        db.session.delete(task_to_be_deleted)
        db.session.commit()
        return jsonify(response={"success": "Successfully Deleted"})
    else:
        return jsonify(response={"error": "Cafe not found"}), 404


def add_task(task_to_be_added):
    new_task = task_to_be_added.to_model()
    db.session.add(new_task)
    db.session.commit()
