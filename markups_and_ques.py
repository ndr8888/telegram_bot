from telegram import ReplyKeyboardMarkup
from db_data.work_with_db import get_questions

main_markup = ReplyKeyboardMarkup(
    [["1-4 классы", "5-11 классы"]], one_time_keyboard=False
)
markup_1 = ReplyKeyboardMarkup(
    [['Помощь', 'Телефон'],
     ['Вопросы', 'Назад'],
     ['Адрес']], one_time_keyboard=False
)
markup_5 = ReplyKeyboardMarkup(
    [['Помощь1', 'Телефон1'],
     ['Вопросы1', 'Назад1'],
     ['Адрес1']], one_time_keyboard=False)

# que_dct_1 = que_dct_5 = {q1[0][1]: q1[0][2], q2[0][1]: q2[0][2], q3[0][1]: q3[0][2], q4[0][1]: q4[0][2],
#                          q5[0][1]: q5[0][2], q6[0][1]: q6[0][2], q7[0][1]: q7[0][2], q8[0][1]: q8[0][2],
#                          q9[0][1]: q9[0][2], q10[0][1]: q10[0][2], q11[0][1]: q11[0][2], q12[0][1]: q12[0][2],
#                          q13[0][1]: q13[0][2], q14[0][1]: q14[0][2], q15[0][1]: q15[0][2]}
que_dct_1 = que_dct_5 = get_questions() # получение данных из бд
markup_q_1 = markup_q_5 = ReplyKeyboardMarkup([['Назад']] + list(map(lambda x: [x], que_dct_1)),
                                              one_time_keyboard=False)
