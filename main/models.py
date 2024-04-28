import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Lists(db.Model):
    __tablename__ = "lists"

    list_id = db.Column(db.String(36), primary_key=True)
    list_name = db.Column(db.String(50), nullable=False, unique=True)


class Tasks(db.Model):
    __tablename__ = "tasks"

    entry_id = db.Column(db.String(36), primary_key=True)
    task_list = db.Column(db.String(20), nullable=False, unique=True)
    heading = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    date_of_creation = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now().date())
