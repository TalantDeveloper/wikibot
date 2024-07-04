from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("7298822162:AAF6PEEkwpYhb6ikJHuT6U37C_lpc2CjXgo").build()

app.add_handler(CommandHandler("start", hello))

app.run_polling()

