from flask_bootstrap import Bootstrap5
from flask import Flask

## defining Flask object
app = Flask(__name__)
app.config["SECRET_KEY"] = "ultrasupersecretkeythatnobodyknows"

## define Bootstrap
Bootstrap5(app)

##  Configs
