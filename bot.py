from telegram.ext import Updater, CommandHandler

updater = Updater(token='1881218661:AAFcllZI3Kf4ivPKlpmUFtC6Zfo88_GbBGc')


def start(update, context):

    updater.message.reply_text("Hello World! sd")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler(command='start', callback=start ))

updater.start_polling()
updater.idle()
