import asyncio
from telegram.ext import Application
from dotenv import load_dotenv
import os
from bot.handlers import setup_handlers

load_dotenv()

async def main():
    """Start the bot."""
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    
    await setup_handlers(application)
    
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())