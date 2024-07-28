from telebot.async_telebot import AsyncTeleBot
from .config import config
import asyncio
import logging

log = logging.getLogger(__name__)
bot = AsyncTeleBot(config["BOT_TOKEN"])


@bot.message_handler(commands=["start"])
async def send_welcome(message):
    text = "Hewwo world! :3"
    await bot.reply_to(message, text)


def bot_main():
    log.debug(".infinity_polling()")
    asyncio.run(bot.polling())
