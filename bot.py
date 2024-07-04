from telegram.ext import Updater, CommandHandler
import key

updater = Updater(key.TOKEN)


def start(update, context):

    updater.message.reply_text("Hello World! sd")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler(command='start', callback=start ))

updater.start_polling()
updater.idle()
