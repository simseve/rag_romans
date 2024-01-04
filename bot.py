import llm_mistral_7b as sellm
import logging
from telegram import Update
from telegram.ext import ContextTypes
import os


logger = logging.getLogger(__name__)

# Global variables to store LLM and chat engine
global_llm = None
global_chat_engine = None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    global global_llm, global_chat_engine
    try:
        logger.info("Initializing the bot...")
        await update.message.reply_text('Please wait patiently now. Initializing the bot...')
        global_llm = sellm.initialize_llm("mistral")
        logger.info("LLM initialized.")
        logger.info("Ingesting documents...")
        global_chat_engine = sellm.ingest_documents("./docs", [".pdf"], global_llm)
        logger.info("Documents ingested.")
        await update.message.reply_text('Hello! I am your chatbot. I am ready to chat now.')
    except Exception as e:
        logger.error(f"Error in start: {e}")
        await update.message.reply_text('Error initializing the bot. Please try again later.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Call Simone Severini for help.")

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Answer the user message."""
    message = update.message.text
    try:
        if global_chat_engine is not None:
            response = sellm.query_chat_engine(global_chat_engine, message)
            logger.info(f"User message: {message} User response: {response.response}")
            await update.message.reply_text(response.response)
        else:
            logger.info("Chat engine is not initialized.")
            await update.message.reply_text("Chat engine is not initialized. Please start the bot with /start command.")
    except Exception as e:
        logger.error(f"Error in answer: {e}")
        await update.message.reply_text("Sorry, there was an error processing your request.")


