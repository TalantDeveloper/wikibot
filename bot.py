from telegram.ext import Updater, CommandHandler

updater = Updater(token='')


def start(update, context):

    updater.message.reply_text("Hello World! sd")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler(command='start', callback=start ))

updater.start_polling()
updater.idle()
