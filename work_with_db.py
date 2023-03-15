import sqlite3

conn = sqlite3.connect('questions.db')
cur = conn.cursor()
que_dct_1 = que_dct_5 = dict([tuple(list(cur.execute(f"""SELECT * FROM questions WHERE id={i}"""))[0][1:]) for i in range(1, 16)])
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