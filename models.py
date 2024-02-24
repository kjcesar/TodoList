from flask_login import UserMixin

# my improts
from app import db


class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    due_date = db.Column(db.Date, default=None)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
