
from enum import unique
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from global_variables import db,app
from sqlalchemy.exc import IntegrityError


    
class Questions(db.Model):
    numer_row = db.Column(db.Integer, primary_key=True,nullable=False)
    id_question = db.Column(db.Integer,nullable=False)
    text_question = db.Column(db.String(1000),nullable=False, unique=True)
    text_answer = db.Column(db.String(1000),nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return '<Questions %r>' % self.text_question

def create_db():
    migrate = Migrate(app, db)
    db.create_all()