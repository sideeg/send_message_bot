import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler, \
    Application, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = '7327423547:AAF4mJGQ7pJk9Il_DYfqiUcSBnQkIoOKR2Q'

# States for the conversation handler
USER_ID, MESSAGE = range(2)


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! Please send the user ID you want to message.')
    return USER_ID


async def get_user_id(update: Update, context: CallbackContext) -> None:
    context.user_data['user_id'] = update.message.text
    await update.message.reply_text('Got it! Now send the message you want to send to the user.')
    return MESSAGE


async def get_message(update: Update, context: CallbackContext) -> None:
    user_id = context.user_data['user_id']
    message = update.message.text

    try:
        await context.bot.send_message(chat_id=user_id, text=message)
        await update.message.reply_text('Message sent!')
    except Exception as e:
        await update.message.reply_text(f'Error: {e}')

    return ConversationHandler.END


async def cancel(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Operation cancelled.')
    return ConversationHandler.END

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Sorry, I didn\'t understand that command.')
def main() -> None:
    # Create the Updater and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()



    # Add conversation handler with the states USER_ID and MESSAGE
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            USER_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_user_id)],
            MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_message)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    application.add_handler(conv_handler)
    # Add handlers for commands
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('cancel', cancel))
    # Start the Bot
    application.run_polling()




if __name__ == '__main__':
    main()
