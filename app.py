from flask_bootstrap import Bootstrap5
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


## defining Flask object
app = Flask(__name__)
app.config["SECRET_KEY"] = "ultrasupersecretkeythatnobodyknows"

## define Bootstrap
Bootstrap5(app)


##  Configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"


## DATABASE
db = SQLAlchemy()
db.init_app(app)
