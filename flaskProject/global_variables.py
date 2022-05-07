from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from instance.config import Config
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
db = SQLAlchemy(app)