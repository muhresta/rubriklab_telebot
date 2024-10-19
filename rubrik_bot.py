import logging
import requests
import os
from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text('Hai aku bot!')
    logging_info(f"Received /start command from chat_id: {chat_id}")
    
async def main() -> None:
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_Handler(CommandHandler("start", start))
    
    await application.run_polling()
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
