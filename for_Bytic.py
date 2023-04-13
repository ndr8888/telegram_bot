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

db_session.global_init('db_data/questions.db')  # инициализация бд

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
        await update.message.reply_text('Выберите интересующий Вас курс', reply_markup=markup_1_2)
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
        await update.message.reply_text(
            f"{desk_1}")
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
    context.chat_data['course'] = update.message.text
    if update.message.text == 'Каллиграфия':
        await update.message.reply_text('Пожалуйста, выберите действие', reply_markup=markup_courses)
        return COURSES
    elif update.message.text == 'Курс1':
        await update.message.reply_text('Пожалуйста, выберите действие', reply_markup=markup_courses)
        return COURSES
    elif update.message.text == 'Курс2':
        await update.message.reply_text('Пожалуйста, выберите действие', reply_markup=markup_courses)
        return COURSES
    elif update.message.text == 'Назад':
        if context.chat_data['courses'] == 1:
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
        if context.chat_data['course'] == 'Каллиграфия':
            await update.message.reply_text('Тут будет информация о курсе Каллиграфии')
        elif context.chat_data['course'] == 'Курс1':
            await update.message.reply_text('Тут будет информация о курсе1')
        elif context.chat_data['course'] == 'Курс2':
            await update.message.reply_text('Тут будет информация о курсе2')
    elif update.message.text == 'Записаться на курс':
        await update.message.reply_text(
            'Записаться на курс можно будет по ссылке: *тут будет ссылка*')
    elif update.message.text == 'Назад':
        await update.message.reply_text(
            'Вы вернулись в предыдущий раздел', reply_markup=markup_1_2)
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
        await update.message.reply_text('Выберите интересующий Вас курс', reply_markup=markup_1_2)
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


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


async def secret_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f'Приветствую, {update.message.chat.last_name} {update.message.chat.first_name}. '
        f'Ты знаешь тайный пароль! Тебе доступен уникальный набор функций! Так используй же их!',
        reply_markup=secret_markup_1)
    return SECRET_MAIN_MENU


async def text_play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'Ой, нет, что-то боязно. Верни меня обратно!':
        await update.message.reply_text('Конечно-конечно! Всё вернётся на круги своя, просто '
                                        'напиши /start', reply_markup=markup_1)
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
    context.chat_data['Player'] = player
    await update.message.reply_text(f'Чтож, {update.message.text}, вот твой профиль:\n'
                                    f'Сила: {context.chat_data["Player"].force}\nЛовкость: {context.chat_data["Player"].agility}\n'
                                    f'Телосложение: {context.chat_data["Player"].physique}\nЗдоровье: {context.chat_data["Player"].hp}\n'
                                    f'Урон: {context.chat_data["Player"].damage}\nОружие:{context.chat_data["Player"].weapon}\n'
                                    f'Пойдём проверим какого-нибудь монстра на прочность?',
                                    reply_markup=markup_go_to_moster)
    return GO_TO_FIRST_MONSTER


async def go_to_first_monster(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'Мне нужно немного времени':
        await update.message.reply_text(
            f'Хорошо, пока что посмотри на свои характеристики и подумай\n\n{context.chat_data["Player"].nick}, вот твой профиль:\n'
            f'Сила: {context.chat_data["Player"].force}\nЛовкость: {context.chat_data["Player"].agility}\n'
            f'Телосложение: {context.chat_data["Player"].physique}\nЗдоровье: {context.chat_data["Player"].hp}\n'
            f'Урон: {context.chat_data["Player"].damage}\nОружие: {context.chat_data["Player"].weapon}\n'
            f'Пойдём проверим какого-нибудь монстра на прочность?',
            reply_markup=markup_go_to_moster_without_run)
    elif update.message.text == 'Вперёд!':
        await update.message.reply_text('Желаю тебе удачи, будет сложно, но ты - ты справишься!!!')
        return FIGHT
    else:
        await update.message.reply_text('Не время для разговоров! Пора идти!')


async def fight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.chat_data['enemy'] = Monster('weak')
    await update.message.reply_text('Бой начался! Действуйте!', reply_markup=markup_for_fight)
    while context.chat_data['enemy'].hp > 0 and context.chat_data['player'].hp > 0:
        if update.message.text == 'Атаковать':
            context.chat_data['enemy'].hp -= context.chat_data['player'].damage
            context.chat_data['player'].hp -= context.chat_data['enemy'].damage
            await update.message.reply_text(f"Вы нанесли противнику {context.chat_data['player'].damage} урона. У него осталось {context.chat_data['enemy'].hp} хп")
            await update.message.reply_text(
                f"Противник нанёс Вам {context.chat_data['enemy'].damage} урона. У Вас осталось {context.chat_data['player'].hp} хп")
        else:
            regen = randint(1, 2)
            await update.message.reply_text(
                f"Вы восстанавливаете {regen} здоровья, но монстр догоняет!!!")
            context.chat_data['player'].hp += regen


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
            ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, address_menu)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True
    )

    secret_handler = ConversationHandler(
        entry_points=[CommandHandler("secret", secret_start)],
        states={
            SECRET_MAIN_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, text_play)],
            REGISTER: [MessageHandler(filters.TEXT & ~filters.COMMAND, register)],
            GO_TO_FIRST_MONSTER: [MessageHandler(filters.TEXT & ~filters.COMMAND, go_to_first_monster)],
            FIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, fight)],
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
