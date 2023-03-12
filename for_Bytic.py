#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging, aiohttp

from telegram import __version__ as TG_VER

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
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
bytic_address = 'Сиреневый бульвар, 11, Троицк, Москва'
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

MAIN_MENU, MENU_1, MENU_5, QUE_1, QUE_5 = range(5)

main_markup = ReplyKeyboardMarkup(
            [["1-4 классы", "5-11 классы"]], one_time_keyboard=False
        )
markup_1 = ReplyKeyboardMarkup(
            [['помощь', 'телефон'],
             ['вопросы', 'назад'],
             ['адрес']], one_time_keyboard=False
        )
markup_5 = ReplyKeyboardMarkup(
            [['помощь1', 'телефон1'],
             ['вопросы1', 'назад1'],
             ['адрес1']], one_time_keyboard=False)

que_dct_1 = que_dct_5 = {'вопрос_1': 'ответ_1', 'вопрос_2': 'ответ_2'}
markup_q_1 = markup_q_5 = ReplyKeyboardMarkup(list(map(lambda x: [x], que_dct_1)) + [['назад']], one_time_keyboard=False)

async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник.")


async def address(update, context):
    await update.message.reply_text(
        "Адрес: г. Москва, ул. Льва Толстого, 16")


async def phone(update, context):
    await update.message.reply_text("Телефон: +7(495)776-3030")


async def site(update, context):
    await update.message.reply_text(
        "Сайт: http://www.yandex.ru/company")


async def work_time(update, context):
    await update.message.reply_text(
        "Время работы: круглосуточно.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE, back=False) -> int:
    # print('start')
    """Starts the conversation and asks the user about their gender."""
    await update.message.reply_text(
        'Выберите нужный вам класс',
        reply_markup=main_markup,
    )
    return MAIN_MENU


async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, back_message=None) -> int:
    """Stores the selected gender and asks for a photo."""
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
    print('menu_1')
    """Stores the photo and asks for a location."""
    if update.message.text == 'помощь':
        await update.message.reply_text(
            "qwerty")
    elif update.message.text == 'телефон':
        await update.message.reply_text(
            "uiop")
    elif update.message.text == 'вопросы':
        await update.message.reply_text(
            'нажмите на вопрос, чтобы получить ответ',
            reply_markup=markup_q_1)
        return QUE_1
    elif update.message.text == 'назад':
        return await start(update, context, back=True)
    elif update.message.text == 'адрес':
        geocoder_uri = "http://geocode-maps.yandex.ru/1.x/"
        response = await get_response(geocoder_uri, params={
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "format": "json",
            "geocode": bytic_address
        })
        toponym = response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        rect = toponym['boundedBy']['Envelope']
        delta = min([abs(float(rect['lowerCorner'].split()[0]) - float(rect['upperCorner'].split()[0])),
                     abs(float(rect['lowerCorner'].split()[1]) - float(rect['upperCorner'].split()[1]))]) / 2
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
        ll, spn = ",".join([toponym_longitude, toponym_lattitude]), ",".join([str(delta), str(delta)]),
        # Можно воспользоваться готовой функцией,
        # которую предлагалось сделать на уроках, посвящённых HTTP-геокодеру.

        static_api_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn}&l=map&pt={','.join([toponym_longitude, toponym_lattitude]) + ',pm2rdl'}"
        await context.bot.send_photo(
            update.message.chat_id,  # Идентификатор чата. Куда посылать картинку.
            # Ссылка на static API, по сути, ссылка на картинку.
            # Телеграму можно передать прямо её, не скачивая предварительно карту.
            static_api_request,
            caption=bytic_address
        )

async def get_response(url, params):
    logger.info(f"getting {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()

async def menu_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # print('menu_5')
    if update.message.text == 'помощь1':
        await update.message.reply_text(
            "qwerty")
    elif update.message.text == 'телефон1':
        await update.message.reply_text(
            "uiop")
    elif update.message.text == 'вопросы1':
        await update.message.reply_text(
            'нажмите на вопрос, чтобы получить ответ',
            reply_markup=markup_q_5)
        return QUE_5
    elif update.message.text == 'назад1':
        return await start(update, context, back=True)
    elif update.message.text == 'адрес1':

        geocoder_uri = "http://geocode-maps.yandex.ru/1.x/"
        response = await get_response(geocoder_uri, params={
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "format": "json",
            "geocode": bytic_address
        })
        toponym = response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        rect = toponym['boundedBy']['Envelope']
        delta = min([abs(float(rect['lowerCorner'].split()[0]) - float(rect['upperCorner'].split()[0])),
                     abs(float(rect['lowerCorner'].split()[1]) - float(rect['upperCorner'].split()[1]))]) / 2
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
        ll, spn = ",".join([toponym_longitude, toponym_lattitude]), ",".join([str(delta), str(delta)]),
        # Можно воспользоваться готовой функцией,
        # которую предлагалось сделать на уроках, посвящённых HTTP-геокодеру.

        static_api_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn}&l=map&pt={','.join([toponym_longitude, toponym_lattitude]) + ',pm2rdl'}"
        await context.bot.send_photo(
            update.message.chat_id,  # Идентификатор чата. Куда посылать картинку.
            # Ссылка на static API, по сути, ссылка на картинку.
            # Телеграму можно передать прямо её, не скачивая предварительно карту.
            static_api_request,
            caption=bytic_address
        )

async def que_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    for que, ans in que_dct_1.items():
        if update.message.text == que:
            await update.message.reply_text(
                ans,
                reply_markup=markup_q_1)
    if update.message.text == 'назад':
        return await main_menu(update, context, back_message='1-4 классы')

async def que_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    for que, ans in que_dct_5.items():
        if update.message.text == que:
            await update.message.reply_text(
                ans,
                reply_markup=markup_q_5)
    if update.message.text == 'назад':
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
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6013111011:AAF8HwDbWB22mjumWf5i3spHsslf3tnjFh8").build()

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
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

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()