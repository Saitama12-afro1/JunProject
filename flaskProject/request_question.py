import json
import requests
from database import Questions
from global_variables import db
from sqlalchemy.exc import IntegrityError
from instance.config import Url_sait



def request_json(count_questions:int,unique_database = True) -> json:
    post_json:json = []
    url = Url_sait.url
    if unique_database:
        for i in range(count_questions):
            
            req = requests.get(url=url)
            post_json.append(json.loads(req.text))

        return post_json
    else :
        req = requests.get(url = url)
        return((json.loads(req.text)))

def add_questions(count_questions:int) -> json: 
    questions:json = request_json(count_questions=count_questions)
    l:int = len(questions)
    for i in range(l):
        try:
            question_in_database = Questions(id_question =int(questions[i][0]["id"]),text_question = questions[i][0]["question"],
                                         text_answer = questions[i][0]["answer"], date = questions[i][0]["airdate"] ) 
            db.session.add(question_in_database)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            questions.append(request_json(count_questions,unique_database = False))
            l += 1
   



            
            