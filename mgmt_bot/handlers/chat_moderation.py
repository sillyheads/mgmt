from telebot.async_telebot import AsyncTeleBot
from telebot import types
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


async def ban_handler(
    message: types.Message,
    bot: AsyncTeleBot
) -> None:
    """Handler for /ban command"""

    if message.reply_to_message:
        user_to_ban = message.reply_to_message.from_user.id
        log.info("Banning %s..." % user_to_ban)
        await bot.ban_chat_member(message.chat.id, user_to_ban)
        await bot.reply_to(message, "Banned %s!" % user_to_ban)
