from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update
from bot import start, help_command, answer  # Importing your handler functions
import os
from dotenv import load_dotenv
import logger_config

# Setup logger
logger_config.setup_logger()

# Load environment variables from .env file
load_dotenv()

# Use the token from the environment
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

if __name__ == '__main__':
    application = Application.builder().token(telegram_bot_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
