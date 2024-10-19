import logging
import requests
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hai aku bot!')
    
def main() -> None:
    Update = Updater(bot_token=BOT_TOKEN)
    dispatcher = updater.dispatcher
    
    dispatcher.add_Handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()
