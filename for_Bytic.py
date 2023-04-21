from db_data import db_session
from logger import *
from CONST import *
from geocode import api_request

from Player import *
from Monsters import *

from telegram import __version__ as TG_VER
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]
if __version_info__ < (20, 0, 0, "alpha", 5):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

db_session.global_init('db_data/questions_and_courses.db')  # инициализация бд

from markups_and_ques import *  # после инициализации импортируем все markupы, не переносить наверх


# помощь
async def help(update, context):
    await update.message.reply_text(
        "Я - бот справочник Байтика.")


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE, back=False) -> int:
    # print('start')
    # Самый старт бота, просит выбрать класс на летнюю программу
    await update.message.reply_text(
        'Выберите нужный вам класс',
        reply_markup=main_markup,
    )
    return MAIN_MENU


# главное меню, просит выбрать вас класс для летней программы
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, back_message=None) -> int:
    # print('main_menu')
    user = update.message.from_user
    if '1-4 классы' in [update.message.text, back_message]:
        await update.message.reply_text(
            "Выберите интересующее Вас направление",
            reply_markup=markup_1)
        return MENU_1
    elif 'дошкольники' in [update.message.text, back_message]:
        await update.message.reply_text(
            "Выберите интересующее Вас направление",
            reply_markup=markup_0)
        return MENU_0
    elif '5-11 классы' in [update.message.text, back_message]:
        await update.message.reply_text(
            "Выберите интересующее Вас направление",
            reply_markup=markup_5)
        return MENU_5
    else:
        await update.message.reply_text(
            "Я Вас не понимаю☹ Пожалуйста, выберите нужный Вам класс")


async def menu_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == 'Летние образовательные смены':
        await update.message.reply_text('Выберите интересующий Вас вопрос', reply_markup=groups)
        return GROUPS_1
    elif update.message.text == 'Летние курсы':
        await update.message.reply_text('Выберите интересующий Вас курс',
                                        reply_markup=markup_course_1)
        context.chat_data['courses'] = 1
        return MENU_1_2
    elif update.message.text == 'Назад':
        return await start(update, context, back=True)
    else:
        await update.message.reply_text(
            "Я Вас не понимаю☹ Пожалуйста, выберите что-нибудь из предложенного списка")


async def groups_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    # сохраняю информацию в словарь, чтобы на основе выбранной группы выводить описание
    context.chat_data['groups'] = update.message.text
    if update.message.text == '1-я смена (29 мая - 9 июня)':
        await update.message.reply_text('Выберите интересующую Вас информацию',
                                        reply_markup=markup_1_1)
        return MENU_1_1
    elif update.message.text == '2-я смена (13 июня - 23 июня)':
        await update.message.reply_text('Выберите интересующую Вас информацию',
                                        reply_markup=markup_1_1)
        return MENU_1_1
    else:
        await update.message.reply_text(
            "Я Вас не понимаю☹ Пожалуйста, выберите интересующую Вас смену")


async def menu_1_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # вывожу описание в зависимости от выбранной группы. Определяется в функции groups_1
    if update.message.text == 'Описание':
        if context.chat_data['groups'] == '1-я смена (29 мая - 9 июня)':
            await update.message.reply_text(
                f"{desk_1}")
        elif context.chat_data['groups'] == '2-я смена (13 июня - 23 июня)':
            await update.message.reply_text(
                f"{desk_2}")
    elif update.message.text == 'Расписание':
        await update.message.reply_text(
            f"{ordinary}")
    elif update.message.text == 'Контакты':
        await update.message.reply_text(
            "Телефон: +74959559470\nЭлектронная почта: bytic@bytic.ru")
    elif update.message.text == 'Стоимость':
        await update.message.reply_text(
            "Стоимость - 2500 за день лагеря; обеды оплачиваются отдельно")
    elif update.message.text == 'Вопросы':
        await update.message.reply_text(
            'Нажмите на вопрос, чтобы получить ответ',
            reply_markup=markup_q_1)
        return QUE_1
    elif update.message.text == 'Назад':
        await update.message.reply_text(
            'Вы вернулись в предыдущий раздел', reply_markup=markup_1)
        return MENU_1
    elif update.message.text == 'Адрес':
        context.chat_data['address'] = 1
        await update.message.reply_text(
            'Выберите филиал Байтика',
            reply_markup=markup_address)

        return ADDRESS
    else:
        await update.message.reply_text(
            "Я Вас не понимаю☹ Пожалуйста, выберите интересующий Вас вопрос")


async def menu_1_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text in list(courses0_dct.keys()) + list(courses1_dct.keys()) + list(
            courses5_dct.keys()):
        context.chat_data['course'] = update.message.text
        await update.message.reply_text('Пожалуйста, выберите действие', reply_markup=markup_courses)
        return COURSES
    elif update.message.text == 'Назад':
        if context.chat_data['courses'] == 0:
            await update.message.reply_text(
                'Вы вернулись в предыдущий раздел', reply_markup=markup_0)
            return MENU_0
        elif context.chat_data['courses'] == 1:
            await update.message.reply_text(
                'Вы вернулись в предыдущий раздел', reply_markup=markup_1)
            return MENU_1
        else:
            await update.message.reply_text(
                'Вы вернулись в предыдущий раздел', reply_markup=markup_5)
            return MENU_5
    else:
        await update.message.reply_text(
            "Я Вас не понимаю☹ Пожалуйста, выберите интересующий Вас курс")


async def courses(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == 'Описание':
        if context.chat_data['courses'] == 0:
            await update.message.reply_text(courses0_dct[context.chat_data['course']][0])
        elif context.chat_data['courses'] == 1:
            await update.message.reply_text(courses1_dct[context.chat_data['course']][0])
        else:
            await update.message.reply_text(courses5_dct[context.chat_data['course']][0])
        # if context.chat_data['course'] == 'Каллиграфия':
        #     await update.message.reply_text('Тут будет информация о курсе Каллиграфии')
        # elif context.chat_data['course'] == 'Курс1':
        #     await update.message.reply_text('Тут будет информация о курсе1')
        # elif context.chat_data['course'] == 'Курс2':
        #     await update.message.reply_text('Тут будет информация о курсе2')
    elif update.message.text == 'Записаться на курс':
        if context.chat_data['courses'] == 0:
            await update.message.reply_text(courses0_dct[context.chat_data['course']][1])
        elif context.chat_data['courses'] == 1:
            await update.message.reply_text(courses1_dct[context.chat_data['course']][1])
        else:
            await update.message.reply_text(courses5_dct[context.chat_data['course']][1])
    elif update.message.text == 'Назад':
        if context.chat_data['courses'] == 0:
            await update.message.reply_text(
                'Вы вернулись в предыдущий раздел', reply_markup=markup_course_0)
            return MENU_1_2
        elif context.chat_data['courses'] == 1:
            await update.message.reply_text(
                'Вы вернулись в предыдущий раздел', reply_markup=markup_course_1)
            return MENU_1_2
        else:
            await update.message.reply_text(
                'Вы вернулись в предыдущий раздел', reply_markup=markup_course_5)
            return MENU_1_2
    else:
        await update.message.reply_text(
            "Я Вас не понимаю☹ Пожалуйста, выберите интересующее Вас действие")


async def address_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == 'Сиреневый бульвар':
        response = await get_response(geocoder_uri, params={
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "format": "json",
            "geocode": bytic_address_1
        })
        await context.bot.send_photo(
            update.message.chat_id,  # Идентификатор чата. Куда посылать картинку.
            # Ссылка на static API, по сути, ссылка на картинку.
            # Телеграму можно передать прямо её, не скачивая предварительно карту.
            api_request(response),
            caption=bytic_address_1
        )
    elif update.message.text == 'Микрорайон В':
        response = await get_response(geocoder_uri, params={
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "format": "json",
            "geocode": bytic_address_2
        })
        await context.bot.send_photo(
            update.message.chat_id,  # Идентификатор чата. Куда посылать картинку.
            # Ссылка на static API, по сути, ссылка на картинку.
            # Телеграму можно передать прямо её, не скачивая предварительно карту.
            api_request(response),
            caption=bytic_address_2
        )
    elif update.message.text == 'Назад':
        if context.chat_data['address'] == 1:
            await update.message.reply_text(
                'Вы вернулись в предыдущий раздел', reply_markup=markup_1_1)
            return MENU_1_1
        else:
            await update.message.reply_text(
                'Вы вернулись в предыдущий раздел', reply_markup=markup_5)
            return MENU_5
    else:
        await update.message.reply_text(
            "Я Вас не понимаю☹ Пожалуйста, выберите интересующий Вас курс")


async def menu_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # print('menu_5')
    if update.message.text == 'Расписание':
        await update.message.reply_text(
            f"{ordinary}")
    elif update.message.text == 'Контакты':
        await update.message.reply_text(
            "Телефон: +74959559470\nЭлектронная почта: bytic@bytic.ru")
    elif update.message.text == 'Стоимость':
        await update.message.reply_text(
            "Стоимость - 2500 за день лагеря")
    elif update.message.text == 'Вопросы':
        await update.message.reply_text(
            'Нажмите на вопрос, чтобы получить ответ',
            reply_markup=markup_q_5)
        return QUE_5
    elif update.message.text == 'Назад':
        return await start(update, context, back=True)
    elif update.message.text == 'Адрес':
        context.chat_data['address'] = 2
        await update.message.reply_text(
            'Выберите филиал Байтика',
            reply_markup=markup_address)
        return ADDRESS
    elif update.message.text == 'Летние курсы':
        await update.message.reply_text('Выберите интересующий Вас курс',
                                        reply_markup=markup_course_5)
        context.chat_data['courses'] = 5
        return MENU_1_2
    else:
        await update.message.reply_text(
            "Я Вас не понимаю☹ Пожалуйста, выберите интересующий Вас вопрос")


async def que_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    for que, ans in que_dct_1.items():
        if update.message.text == que:
            await update.message.reply_text(
                ans)
    if update.message.text == 'Назад':
        await update.message.reply_text(
            'Вы вернулись в предыдущий раздел', reply_markup=markup_1_1)
        return MENU_1_1


async def que_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    for que, ans in que_dct_5.items():
        if update.message.text == que:
            await update.message.reply_text(
                ans,
                reply_markup=markup_q_5)
    if update.message.text == 'Назад':
        return await main_menu(update, context, back_message='5-11 классы')


async def menu_0(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == 'Летние курсы':
        await update.message.reply_text('Выберите интересующий Вас курс',
                                        reply_markup=markup_course_0)
        context.chat_data['courses'] = 0
        return MENU_1_2
    elif update.message.text == 'Назад':
        return await start(update, context, back=True)
    else:
        await update.message.reply_text(
            "Я Вас не понимаю☹ Пожалуйста, выберите интересующий Вас вопрос")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Информация сброшена", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


async def secret_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f'Приветствую, {update.message.chat.last_name} {update.message.chat.first_name}. '
        f'Ты знаешь тайный пароль! Тебе доступен уникальный набор функций! Так используй же их!\nP.S если Вы уже использовали команду /start, для продолжения напишите /cancel, а потом снова /secret',
        reply_markup=secret_markup_1)
    return SECRET_START_MENU


async def text_play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'Ой, нет, что-то боязно. Верни меня обратно!':
        await update.message.reply_text('Конечно-конечно! Всё вернётся на круги своя, просто '
                                        'напиши /start', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    if update.message.text == 'Ничего себе! Конечно использовать!':
        await update.message.reply_text('Тогда мы начинаем! Как тебя называть?',
                                        reply_markup=ReplyKeyboardRemove())
        return REGISTER
    else:
        await update.message.reply_text('Непонятно☹. Пожалуйста, выберите что-то из предложенного '
                                        'списка')


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    player = Player(update.message.text)
    context.chat_data['player'] = player
    await update.message.reply_text(f'Чтож, {update.message.text}, вот твой профиль:\n'
                                    f'Сила: {context.chat_data["player"].force}\nЛовкость: {context.chat_data["player"].agility}\n'
                                    f'Телосложение: {context.chat_data["player"].physique}\nЗдоровье: {context.chat_data["player"].hp}\n'
                                    f'Урон: {context.chat_data["player"].damage}\nОружие: {context.chat_data["player"].weapon}\n'
                                    f'Пойдём проверим какого-нибудь монстра на прочность?',
                                    reply_markup=markup_go_to_moster)
    return GO_TO_FIRST_MONSTER


async def go_to_first_monster(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'Мне нужно немного времени':
        await update.message.reply_text(
            f'Хорошо, пока что посмотри на свои характеристики и подумай\n\n{context.chat_data["player"].nick}, вот твой профиль:\n'
            f'Сила: {context.chat_data["player"].force}\nЛовкость: {context.chat_data["player"].agility}\n'
            f'Телосложение: {context.chat_data["player"].physique}\nЗдоровье: {context.chat_data["player"].hp}\n'
            f'Урон: {context.chat_data["player"].damage}\nОружие: {context.chat_data["player"].weapon}\n'
            f'Пойдём проверим какого-нибудь монстра на прочность?',
            reply_markup=markup_go_to_moster_without_run)
    elif update.message.text == 'Вперёд!':
        context.chat_data['last_message'] = update.message.text
        await update.message.reply_text('Желаю тебе удачи, будет сложно, но ты - ты справишься!!!')
        await update.message.reply_text('Перед тобой небольшой монстрик. Бой начался!',
                                        reply_markup=markup_for_fight)
        return FIRST_FIGHT
    else:
        await update.message.reply_text('Не время для разговоров! Пора идти!')


async def first_fight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.chat_data['last_message'] == 'Вперёд!':
        context.chat_data['enemy'] = Monster('weak')
        context.chat_data['spawn'] = 0
    context.chat_data['last_id'] = update.message.id
    if context.chat_data['player'].hp > 0 and context.chat_data['enemy'].hp > 0:
        if update.message.text == 'Атаковать':
            context.chat_data['enemy'].hp -= context.chat_data['player'].damage
            context.chat_data['player'].hp -= context.chat_data['enemy'].damage
            if context.chat_data['enemy'].hp < 0:
                context.chat_data['enemy'].hp = 0
            await update.message.reply_text(
                f"Вы нанесли противнику {context.chat_data['player'].damage} урона. У него осталось {context.chat_data['enemy'].hp} хп")
            if context.chat_data['enemy'].hp > 0:
                await update.message.reply_text(
                    f"Противник нанёс Вам {context.chat_data['enemy'].damage} урона. У Вас осталось {context.chat_data['player'].hp} хп")
        elif update.message.text == 'Бежать':
            regen = randint(1, 2)
            if context.chat_data['player'].hp != context.chat_data['player'].max_hp:
                if context.chat_data['player'].hp + regen > context.chat_data['player'].max_hp:
                    context.chat_data['player'].hp = context.chat_data['player'].max_hp
                else:
                    context.chat_data['player'].hp += regen
                await update.message.reply_text(
                    f"Вы восстанавливаете {regen} здоровья и теперь его у вас {context.chat_data['player'].hp}, но монстр догоняет!!!")
            else:
                await update.message.reply_text(
                    f"У вас максимальное количество здоровья, но монстр уже близко!")
    if context.chat_data['enemy'].hp == 0:
        await update.message.reply_text(
            f'Это было невероятно трудно, но ты справился! Вы получили: {", ".join([" - ".join([key, str(context.chat_data["enemy"].drop[key])]) for key in context.chat_data["enemy"].drop.keys()])}',
            reply_markup=continue_markup)
        for loot in context.chat_data['enemy'].drop.keys():
            if loot in context.chat_data['player'].inventory.keys():
                context.chat_data['player'].inventory[loot] += context.chat_data['enemy'].drop[loot]
            else:
                context.chat_data['player'].inventory[loot] = context.chat_data['enemy'].drop[loot]
        context.chat_data.pop('enemy', None)
        return MAIN_GAME_MENU
    elif context.chat_data['player'].hp == 0:
        await update.message.reply_text(
            'Ты погиб. Чтож, у всех бывают неудачи, что поделать. Я тебя спас, но я не всегда буду рядом')
        return MAIN_GAME_MENU
    context.chat_data['last_message'] = update.message.text


async def game_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'Идём на базу!':
        await update.message.reply_text(
            f'Поздравляю тебя, {context.chat_data["player"].nick}, ты прошел курс молодого охотника и теперь готов ко всему. Дальше ты будешь действовать сам, и, кто знает, возможно, тебя однажды возьмут к нам в Гильдию?',
            reply_markup=main_game_markup)
        context.chat_data['last_message'] = ''
    elif update.message.text == 'Вернуться на базу':
        await update.message.reply_text(
            f'Ты на базе',
            reply_markup=main_game_markup)
    elif update.message.text == 'Инвентарь':
        await update.message.reply_text(
            f'Ваш инвентарь: {", ".join([" - ".join([key, str(context.chat_data["player"].inventory[key])]) for key in context.chat_data["player"].inventory.keys()])}')
    elif update.message.text == 'Профиль':
        await update.message.reply_text(f'Вот твой профиль:\n'
                                        f'Сила: {context.chat_data["player"].force}\nЛовкость: {context.chat_data["player"].agility}\n'
                                        f'Телосложение: {context.chat_data["player"].physique}\nЗдоровье: {context.chat_data["player"].hp}\n'
                                        f'Урон: {context.chat_data["player"].damage}\nОружие: {context.chat_data["player"].weapon}\n'
                                        f'Активные задания: {", ".join(context.chat_data["player"].kvests)}')
    elif update.message.text == 'Таверна':
        await update.message.reply_text(
            f'Владелец: — Привет, {context.chat_data["player"].nick}. Дело ищешь или желаешь посмотреть на товар?',
            reply_markup=barmen_markup)
        return BARMEN
    elif update.message.text == 'Отправиться на охоту' or update.message.text == 'Продолжить охоту':
        int_monster = randint(1, 100)
        if int_monster > 70:
            await update.message.reply_text(
                'Вам повезло (или нет) и вы наконец встретили Абракабра! Тут Вам помогут лишь Ваша удача и сноровка. Убежать нельзя, бой!',
                reply_markup=markup_for_top_fight)
            context.chat_data['enemy'] = Monster('Abrakabr')
            return USUAL_FIGHT
        elif int_monster < 70:
            await update.message.reply_text('Вы снова встретили монстрика',
                                            reply_markup=markup_for_fight)
            context.chat_data['enemy'] = Monster('weak')
            return USUAL_FIGHT


async def barmen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'Магазин':
        await update.message.reply_text(
            f'Выбирай, вот список товара:\n{"".join([i for i in assortment])}',
            reply_markup=assortment_markup)
        return ASSORTMENT
    elif update.message.text == 'Задание' and context.chat_data['player'].active_quest:
        await update.message.reply_text(
            'Раз ты дошел сюда - значит, уже чего-то стоишь. Но задание не из простых: в лесах завёлся Абракабр. '
            'Злобная животина, скажу я тебе. И очень сильная. Чтобы с ней справиться - я дам тебе один флакончик: '
            'восстановит тебе разом все здоровье. Смотри, не погибни там!')
        await update.message.reply_text(
            f'❗ Получено задание! Очистить лес от Абракабра. Способ: вариативно\n'
            f'P.S: информацию о заданиях вы можете узнать в профиле',
            reply_markup=main_game_markup)
        context.chat_data['player'].kvests += ['Очистить лес от Абракабра. Способ: вариативно']
        context.chat_data['player'].active_quest -= 1
        context.chat_data['player'].inventory['зелье исцеления'] = 1
        return MAIN_GAME_MENU
    elif update.message.text == 'Задание' and context.chat_data['player'].active_quest == 0:
        await update.message.reply_text(f'Дел пока нет, зайди ко мне позже',
                                        reply_markup=main_game_markup)
        return MAIN_GAME_MENU


async def assortiment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'Назад':
        await update.message.reply_text('Вы вернулись в главное меню', reply_markup=main_game_markup)
        return MAIN_GAME_MENU
    elif update.message.text in [i.split(' - ')[0] for i in assortment]:
        cost = int(
            "".join([i.split(' - ')[1].split()[0] for i in assortment if
                     i.split(' - ')[0] == update.message.text]))
        if context.chat_data['player'].inventory['золотые монеты'] >= cost:
            context.chat_data['player'].inventory['золотые монеты'] -= cost
            text_cost = golden.make_agree_with_number(cost).word + ' ' + coin.make_agree_with_number(
                cost).word
            golden_coins = golden.make_agree_with_number(
                context.chat_data["player"].inventory[
                    "золотые монеты"]).word + ' ' + coin.make_agree_with_number(
                context.chat_data["player"].inventory["золотые монеты"]).word
            # с помощью библиотеки pymorphy2 слова пишутся правильно в соответствии с количеством монет
            await update.message.reply_text(
                f'С вашего счёта списана сумма в размере {cost} {text_cost}\nУ вас осталось '
                f'{context.chat_data["player"].inventory["золотые монеты"]} {golden_coins}')
            if 'Лишние оружия' in context.chat_data['player'].inventory.keys():
                if context.chat_data['player'].weapon != 'Кулак':
                    context.chat_data['player'].inventory['Лишние оружия'] += [
                        context.chat_data['player'].weapon]
            else:
                if context.chat_data['player'].weapon != 'Кулак':
                    context.chat_data['player'].inventory['Лишние оружия'] = [
                        context.chat_data['player'].weapon]
            context.chat_data['player'].weapon = "".join(
                [i.split(' - ')[0] for i in assortment if i.split(' - ')[0] == update.message.text])
            with open('weapons_damage.txt', 'r', encoding='utf-8') as dam:
                context.chat_data['player'].damage = int(
                    "".join([i.split(' - ')[1] for i in dam.readlines() if
                             i.split(' - ')[0] == context.chat_data['player'].weapon])) + \
                                                     context.chat_data[
                                                         'player'].force
        else:
            golden_coins = golden.make_agree_with_number(
                context.chat_data["player"].inventory[
                    "золотые монеты"]).word + ' ' + coin.make_agree_with_number(
                context.chat_data["player"].inventory["золотые монеты"]).word
            await update.message.reply_text(
                f'Не хватает денег, на вашем счету {context.chat_data["player"].inventory["золотые монеты"]} {golden_coins}')


async def usual_fight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.chat_data['player'].hp > 0 and context.chat_data['enemy'].hp > 0:
        if update.message.text == 'Атаковать':
            context.chat_data['enemy'].hp -= context.chat_data['player'].damage
            context.chat_data['player'].hp -= context.chat_data['enemy'].damage
            if context.chat_data['enemy'].hp < 0:
                context.chat_data['enemy'].hp = 0
            if context.chat_data['player'].hp < 0:
                context.chat_data['player'].hp = 0
            await update.message.reply_text(
                f"Вы нанесли противнику {context.chat_data['player'].damage} урона. У него осталось {context.chat_data['enemy'].hp} хп")
            if context.chat_data['enemy'].hp > 0:
                await update.message.reply_text(
                    f"Абракабр нанёс Вам {context.chat_data['enemy'].damage} урона. У Вас осталось {context.chat_data['player'].hp} хп")
        elif update.message.text == 'Зелье исцеления' and context.chat_data[
            'enemy'].name == 'abrakabr':
            if context.chat_data['player'].inventory['зелье исцеления'] > 0:
                context.chat_data['player'].hp = context.chat_data['player'].max_hp
                context.chat_data['player'].inventory['зелье исцеления'] -= 1
                await update.message.reply_text(
                    f'Вы восстановили полное здоровье. Теперь у вас его {context.chat_data["player"].max_hp}')
        elif update.message.text == 'Бежать':
            if context.chat_data['enemy'].name == 'abrakabr':
                await update.message.reply_text('От Абракабра не убежать! Сражайся!!!')
            elif context.chat_data['enemy'].name == 'weak':
                regen = randint(1, 2)
                if context.chat_data['player'].hp != context.chat_data['player'].max_hp:
                    if context.chat_data['player'].hp + regen > context.chat_data['player'].max_hp:
                        context.chat_data['player'].hp = context.chat_data['player'].max_hp
                    else:
                        context.chat_data['player'].hp += regen
                    await update.message.reply_text(
                        f"Вы восстанавливаете {regen} здоровья и теперь его у вас {context.chat_data['player'].hp}, но монстр догоняет!!!")
                else:
                    await update.message.reply_text(
                        f"У вас максимальное количество здоровья, но монстр уже близко!")
            else:
                await update.message.reply_text('У вас нет зелий исцеления :(')

    if context.chat_data['enemy'].hp == 0 and context.chat_data['enemy'].name != 'abrakabr':
        await update.message.reply_text(
            f'Это было невероятно трудно, но ты справился! Вы получили: {", ".join([" - ".join([key, str(context.chat_data["enemy"].drop[key])]) for key in context.chat_data["enemy"].drop.keys()])}',
            reply_markup=hunting_markup)
        for loot in context.chat_data['enemy'].drop.keys():
            context.chat_data['player'].inventory[loot] += context.chat_data['enemy'].drop[loot]
        context.chat_data.pop('enemy', None)
        return MAIN_GAME_MENU
    elif context.chat_data['enemy'].hp == 0 and context.chat_data['enemy'].name == 'abrakabr':
        await update.message.reply_text(
            f'Ты победил настоящее чудовище! Ты - ГЕРОЙ!!!\n✔️ Задание "Очистить лес от Абракабра" завершено\n'
            f'Вы получили: {", ".join([" - ".join([key, str(context.chat_data["enemy"].drop[key])]) for key in context.chat_data["enemy"].drop.keys()])}',
            reply_markup=main_game_markup)
        for index, kvest in enumerate(context.chat_data['player'].kvests):
            if 'Абракабр' in kvest:
                del context.chat_data['player'].kvests[index]
        for loot in context.chat_data['enemy'].drop.keys():
            context.chat_data['player'].inventory[loot] += context.chat_data['enemy'].drop[loot]
        context.chat_data.pop('enemy', None)
        return MAIN_GAME_MENU
    elif context.chat_data['player'].hp == 0:
        await update.message.reply_text(
            'Ты погиб, но не навсегда. У тебя ещё будет возможность взять реванш\nВаше здоровье восстановлено',
            reply_markup=main_game_markup)
        context.chat_data['player'].hp = context.chat_data['player'].max_hp
        return MAIN_GAME_MENU
    context.chat_data['last_message'] = update.message.text


def main() -> None:
    """Run the bot."""

    # передаем токен и создаем экземпляр класса Application
    application = Application.builder().token(TOKEN).build()

    # Возвращает цифры, с помощью которых понимает, какую клавиатуру выводить пользователю
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu)],  # главное меню
            MENU_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu_1)],
            # выбор для 1-4 класса
            GROUPS_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, groups_1)],  # выбор смены
            MENU_1_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu_1_1)],
            # летние программы
            MENU_1_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu_1_2)],  # летние курсы
            COURSES: [MessageHandler(filters.TEXT & ~filters.COMMAND, courses)],
            MENU_5: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu_5)],
            # летние программы 5-11
            QUE_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, que_1)],  # вопросы 1-4
            QUE_5: [MessageHandler(filters.TEXT & ~filters.COMMAND, que_5)],  # вопросы 5-11
            ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, address_menu)],
            MENU_0: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu_0)],

        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True
    )

    secret_handler = ConversationHandler(
        entry_points=[CommandHandler("secret", secret_start)],
        states={
            SECRET_START_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, text_play)],
            REGISTER: [MessageHandler(filters.TEXT & ~filters.COMMAND, register)],
            GO_TO_FIRST_MONSTER: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, go_to_first_monster)],
            FIRST_FIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_fight)],
            MAIN_GAME_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, game_main_menu)],
            BARMEN: [MessageHandler(filters.TEXT & ~filters.COMMAND, barmen)],
            ASSORTMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, assortiment)],
            USUAL_FIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, usual_fight)]
        },
        fallbacks=[CommandHandler("qwdqdqwdqwdqwdwdqdwqdas", que_1)],  # тут написана дичь
        allow_reentry=True
    )
    # добавляем в application наш ConversationHandler
    application.add_handler(conv_handler)
    application.add_handler(secret_handler)

    # включаем бота
    application.run_polling()


if __name__ == "__main__":
    main()
