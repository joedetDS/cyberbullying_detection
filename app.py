import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler,CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather
TOKEN = '6510413918:AAELzEGfvLVXZXUPnjqraV8zjubVB_NX4lw'

async def start(update: Update, context: CallbackContext):
    await context.bot.send_message( chat_id=update.effective_chat.id, text=f"This is a cyber bullying bot, I Will help you remove users who engage in cyber-bullying on your group chats")

def main():
    # Create an Updater for your bot

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register the command handler for the "/start" command
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
