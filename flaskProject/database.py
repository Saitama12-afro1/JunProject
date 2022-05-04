
from enum import unique
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



def data_bases(db, app):
    migrate = Migrate(app, db)

    class Users(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.username
        
    class Questions(db.Model):
        id_question = db.Column(db.Integer, primary_key=True)
        text_question = db.Column(db.String(250),nullable=False, unique=True)
        id_answer = db.Column(db.String(250),nullable=False)
        data = db.Column(db.DateTime, nullable=False)
        
        def __repr__(self):
            return '<Questions %r>' % self.text_question

  
    db.create_all()