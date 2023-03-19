from db_data import db_session
from logger import *
from CONST import *
from geocode import api_request
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

db_session.global_init('db_data/questions.db') # инициализация бд

from markups_and_ques import * # после инициализации импортируем все markupы


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
            "Выберите нужное вам действие",
            reply_markup=markup_1)
        return MENU_1
    elif '5-11 классы' in [update.message.text, back_message]:
        await update.message.reply_text(
            "Выберите нужное вам действие",
            reply_markup=markup_5)
        return MENU_5


async def menu_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == 'Расписание':
        await update.message.reply_text(
            f"{ordinary}")
    elif update.message.text == 'Контакты':
        await update.message.reply_text(
            "Телефон: +84958510367")
    elif update.message.text == 'Стоимость':
        await update.message.reply_text(
            "Стоимость - 2500 за день лагеря")
    elif update.message.text == 'Вопросы':
        await update.message.reply_text(
            'Нажмите на вопрос, чтобы получить ответ',
            reply_markup=markup_q_1)
        return QUE_1
    elif update.message.text == 'Назад':
        return await start(update, context, back=True)
    elif update.message.text == 'Адрес':
        response = await get_response(geocoder_uri, params={
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "format": "json",
            "geocode": bytic_address
        })
        await context.bot.send_photo(
            update.message.chat_id,  # Идентификатор чата. Куда посылать картинку.
            # Ссылка на static API, по сути, ссылка на картинку.
            # Телеграму можно передать прямо её, не скачивая предварительно карту.
            api_request(response),
            caption=bytic_address
        )


async def menu_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # print('menu_5')
    if update.message.text == 'Расписание':
        await update.message.reply_text(
            f"{ordinary}")
    elif update.message.text == 'Контакты':
        await update.message.reply_text(
            "Телефон: +84958510367")
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
        response = await get_response(geocoder_uri, params={
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "format": "json",
            "geocode": bytic_address
        })
        await context.bot.send_photo(
            update.message.chat_id,  # Идентификатор чата. Куда посылать картинку.
            # Ссылка на static API, по сути, ссылка на картинку.
            # Телеграму можно передать прямо её, не скачивая предварительно карту.
            api_request(response),
            caption=bytic_address
        )


async def que_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    for que, ans in que_dct_1.items():
        if update.message.text == que:
            await update.message.reply_text(
                ans,
                reply_markup=markup_q_1)
    if update.message.text == 'Назад':
        return await main_menu(update, context, back_message='1-4 классы')


async def que_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    for que, ans in que_dct_5.items():
        if update.message.text == que:
            await update.message.reply_text(
                ans,
                reply_markup=markup_q_5)
    if update.message.text == 'Назад':
        return await main_menu(update, context, back_message='5-11 классы')


# async def skip_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Skips the location and asks for info about the user."""
#     user = update.message.from_user
#     logger.info("User %s did not send a location.", user.first_name)
#     await update.message.reply_text(
#         "You seem a bit paranoid! At last, tell me something about yourself."
#     )
#
#     return BIO


# async def bio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Stores the info about the user and ends the conversation."""
#     user = update.message.from_user
#     logger.info("Bio of %s: %s", user.first_name, update.message.text)
#     await update.message.reply_text("Thank you! I hope we can talk again some day.")
#
#     return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""

    # передаем токен и создаем экземпляр класса Application
    application = Application.builder().token(TOKEN).build()

    # Возвращает цифры, с помощью которых понимает, какую клавиатуру выводить пользователю
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu)],
            MENU_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu_1)],
            MENU_5: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu_5)],
            QUE_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, que_1)],
            QUE_5: [MessageHandler(filters.TEXT & ~filters.COMMAND, que_5)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True
    )
    # добавляем в application наш ConversationHandler
    application.add_handler(conv_handler)

    # включаем бота
    application.run_polling()


if __name__ == "__main__":
    main()
