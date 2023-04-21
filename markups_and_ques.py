from telegram import ReplyKeyboardMarkup
from db_data.work_with_db import get_questions, get_courses_0, get_courses_1, get_courses_5

main_markup = ReplyKeyboardMarkup(
    [["1-4 классы", "5-11 классы", 'дошкольники']], one_time_keyboard=False
)

# предлагает выбрать смену
groups = ReplyKeyboardMarkup([['1-я смена (29 мая - 9 июня)'],
                              ['2-я смена (13 июня - 23 июня)']], one_time_keyboard=False)

# меню с выбором действий для 1-4 классов
markup_1 = ReplyKeyboardMarkup(
    [['Летние образовательные смены'],
     ['Летние курсы'],
     ['Назад']], one_time_keyboard=False)

# меню вопросов для летних образовательных программ для 1-4 классов
markup_1_1 = ReplyKeyboardMarkup(
    [['Описание', 'Стоимость', 'Расписание'],
     ['Вопросы', 'Адрес', 'Контакты'],
     ['Назад']], one_time_keyboard=False)

# меню вопросов для летних курсов

# пока что просто вопросы для 5-11 классов
markup_5 = markup_0 = ReplyKeyboardMarkup(
    [['Летние курсы'],
     ['Назад']], one_time_keyboard=False)

markup_courses = ReplyKeyboardMarkup(
    [['Описание'],
     ['Записаться на курс'],
     ['Назад']], one_time_keyboard=False)

markup_address = ReplyKeyboardMarkup(
    [['Сиреневый бульвар'], ['Микрорайон В'],
     ['Назад']], one_time_keyboard=False)
# ['Микрорайон В'],

que_dct_1 = que_dct_5 = get_questions()  # получение данных из б
courses0_dct = get_courses_0()
courses1_dct = get_courses_1()
courses5_dct = get_courses_5()
markup_course_0 = ReplyKeyboardMarkup([['Назад']] + list(map(lambda x: [x], courses0_dct)),
                                      one_time_keyboard=False)
markup_course_1 = ReplyKeyboardMarkup([['Назад']] + list(map(lambda x: [x], courses1_dct)),
                                      one_time_keyboard=False)
markup_course_5 = ReplyKeyboardMarkup([['Назад']] + list(map(lambda x: [x], courses5_dct)),
                                      one_time_keyboard=False)

markup_q_1 = markup_q_5 = ReplyKeyboardMarkup([['Назад']] + list(map(lambda x: [x], que_dct_1)),
                                              one_time_keyboard=False)

secret_markup_1 = ReplyKeyboardMarkup([['Ничего себе! Конечно использовать!'],
                                       ['Ой, нет, что-то боязно. Верни меня обратно!']])

markup_go_to_moster = ReplyKeyboardMarkup([['Вперёд!'], ['Мне нужно немного времени']])
markup_go_to_moster_without_run = ReplyKeyboardMarkup([['Вперёд!']])
markup_for_fight = ReplyKeyboardMarkup([['Атаковать'], ['Бежать']])
main_game_markup = ReplyKeyboardMarkup(
    [['Отправиться на охоту'], ['Инвентарь', 'Профиль'], ['Таверна']])
continue_markup = ReplyKeyboardMarkup([['Идём на базу!']])
barmen_markup = ReplyKeyboardMarkup([['Магазин'], ['Задание']])
markup_for_top_fight = ReplyKeyboardMarkup([['Атаковать'], ['Зелье исцеления']])
with open('assortment.txt', 'r', encoding='utf-8') as assort:
    assortment = assort.readlines()
assortment_markup = ReplyKeyboardMarkup([[i.split(' - ')[0]] for i in assortment + ['Назад']])
hunting_markup = ReplyKeyboardMarkup([['Вернуться на базу'], ['Продолжить охоту']])
