from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import InputRequired


class TaskForm(FlaskForm):
    task = StringField("Enter a Task")  # , [InputRequired()])
    submit = SubmitField("Add Task")


class DoneForm(FlaskForm):
    done = SubmitField("Done")
    undone = SubmitField("Undone")
    delete = SubmitField("Remove")
