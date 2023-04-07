# Импортируем необходимые классы.
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup

BOT_TOKEN = '6214503286:AAF7uREMKI8Dx9AwcRhWnoxVnBlRNDB175o'
TIMER = 5  # таймер на 5 секунд


async def start(update, context):
    name = update.message.chat.last_name
    await update.message.reply_text(
        f"Здравствуйте! Вы находитесь около музея Александра, желаете войти внутрь, {name}?",
        reply_markup=ReplyKeyboardMarkup([['Войти'], ['Не входить']]))
    return 2


async def hello(update, context):
    name = update.message.chat.last_name
    await update.message.reply_text(
        f"Здравствуйте, {name}. Желаете начать экскурсию?",
        reply_markup=ReplyKeyboardMarkup([['Войти'], ['Не входить']]))
    return 2


async def second(update, context):
    weather = update.message.text
    await update.message.reply_text(
        "Внутри вы можете увидеть столько интересного! Вот, к примеру, наши экспонаты - древние перфоленты",
        reply_markup=ReplyKeyboardMarkup([['Спасибо, давайте дальше']]))
    return 3


async def trird(update, context):
    await update.message.reply_text(
        "А тут вы можете увидеть старые компьтеры. Так они выглядели 20 лет назад. Совсем не так, как сейчас, верно?",
        reply_markup=ReplyKeyboardMarkup(
            [['Да уж, круто, пойдемте скорее дальше!'], ['Что-то я устал, давайте пойдем домой?']]))
    return 4


async def forth(update, context):
    if update.message.text == 'Что-то я устал, давайте пойдем домой?':
        await update.message.reply_text(
            "Хорошо, я Вас провожу ко входу",
            reply_markup=ReplyKeyboardMarkup([['Войти'], ['Не входить']]))
        return 1
    else:
        await update.message.reply_text(
            "Вот мы уже и подходим к концу. Спасибо что пришли! На следующей неделе у нас будут новые экспонаты! Ждем ещё раз в гости!",
            reply_markup=ReplyKeyboardMarkup([['Спасибо']]))
        return 1


async def end(update, context):
    await update.message.reply_text('')


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, hello)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, second)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, trird)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, forth)],
        },
        fallbacks=[CommandHandler('stop', stop), CommandHandler('skip', stop)],
    )
    application.add_handler(conv_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
