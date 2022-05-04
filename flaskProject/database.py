import configparser

import sqlalchemy
from main import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


config = configparser.ConfigParser()
config.sections()

config.read("JunProject/config.ini")
app.config["SQLALCHEMY_DATABASE_URI"] = config["secret"]["UrlDataBase"] 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
db.create_all() 

admin = User(username = "SSSss",email="@")
db.session.add(admin)
db.session.commit()