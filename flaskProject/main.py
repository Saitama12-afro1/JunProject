from distutils.debug import DEBUG
from pickle import TRUE
from flask import render_template, request
from  global_variables import db,app
from database import create_db
from request_question import add_questions
from database import Questions
import json
from sqlalchemy import desc
from instance.config import Config

create_db()

@app.route('/', methods=['POST', 'GET'])   
def index():
 
    question = Questions.query.order_by(desc(Questions.numer_row)).first()
    if request.method == "POST":
        try:
            question = Questions.query.order_by(desc(Questions.numer_row)).first()
            count_question:int = int(request.form.get("title"))
            add_questions(count_question)
           
        except ValueError:
            db.session.rollback()
            question = 0
    return render_template("index.html", question = question)


if __name__ == "__main__":
    app.run(debug=True)