from . import db_session
from db_data.questions import Questions
from db_data.courses_0 import Courses0
from db_data.courses_1 import Courses1
from db_data.courses_5 import Courses5


def get_questions():  # получить словарь вопросов и ответов
    db_sess = db_session.create_session()
    return dict(map(lambda x: (x.quest, x.ans), db_sess.query(Questions).all()))

def get_courses_0():  # получить словарь вопросов и ответов
    db_sess = db_session.create_session()
    return dict(map(lambda x: (x.name, (x.description, x.link)), db_sess.query(Courses0).all()))

def get_courses_1():  # получить словарь вопросов и ответов
    db_sess = db_session.create_session()
    return dict(map(lambda x: (x.name, (x.description, x.link)), db_sess.query(Courses1).all()))

def get_courses_5():  # получить словарь вопросов и ответов
    db_sess = db_session.create_session()
    return dict(map(lambda x: (x.name, (x.description, x.link)), db_sess.query(Courses5).all()))

# import sqlite3

# conn = sqlite3.connect('questions_and_courses.db')
# cur = conn.cursor()
# que_dct_1 = que_dct_5 = dict([tuple(list(cur.execute(f"""SELECT * FROM questions WHERE id={i}"""))[0][1:]) for i in range(1, 16)])

# q1 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=1""")]
# q2 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=2""")]
# q3 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=3""")]
# q4 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=4""")]
# q5 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=5""")]
# q6 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=6""")]
# q7 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=7""")]
# q8 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=8""")]
# q9 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=9""")]
# q10 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=10""")]
# q11 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=11""")]
# q12 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=12""")]
# q13 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=13""")]
# q14 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=14""")]
# q15 = [i for i in cur.execute(f"""SELECT * FROM questions WHERE id=15""")]
# print(q1[0][1])
