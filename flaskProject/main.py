from distutils.debug import DEBUG
from distutils.log import debug
from flask import Flask, session,render_template
import os
from instance.config import Config
from database import data_bases
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__, instance_relative_config=True)
# app.config.from_pyfile("config.py", silent=True)
app.config.from_object(Config)
db = SQLAlchemy(app)

data_bases(db,app)  

@app.route("/")
def hello_word():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)