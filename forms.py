from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, InputRequired


class TaskForm(FlaskForm):
    task = StringField("Enter a Task")  # , [InputRequired()])
    submit = SubmitField("Add Task")


class DoneForm(FlaskForm):
    done = BooleanField(label="DefaultLabel")
    complete = SubmitField("Complete")
    remove = SubmitField("Remove")

    def validate_complete(self, field):
        if self.complete.data:
            if not field.data:
                raise ValidationError("You must check the box to complete the tasks")
