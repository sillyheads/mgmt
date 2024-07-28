from telebot.async_telebot import AsyncTeleBot
from telebot import types
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


async def _ban_user(
    message: types.Message,
    user_to_ban: types.User,
    bot: AsyncTeleBot,
) -> None:
    log.info("Banning %s..." % user_to_ban.id)
    await bot.ban_chat_member(message.chat.id, user_to_ban.id)
    await bot.reply_to(message, "Banned %s" % user_to_ban.first_name)


async def _kick_user(
    message: types.Message,
    user_to_kick: types.User,
    bot: AsyncTeleBot,
) -> None:
    log.info("Kicking %s..." % user_to_kick.id)
    await bot.kick_chat_member(message.chat.id, user_to_kick.id)
    await bot.reply_to(message, "Kicked %s" % user_to_kick.first_name)


async def ban_handler(
    message: types.Message,
    bot: AsyncTeleBot
) -> None:
    """Handler for /ban command"""
    args = message.text.split()
    log.debug(args)

    if message.reply_to_message:
        user_to_ban = message.reply_to_message.from_user
        _ban_user(message, user_to_ban, bot)


async def kick_handler(
    message: types.Message,
    bot: AsyncTeleBot
) -> None:
    """Handler for /kick command"""
    args = message.text.split()
    log.debug(args)

    if message.reply_to_message:
        user_to_kick = message.reply_to_message.from_user
        _kick_user(message, user_to_kick, bot)


__all__ = [
    "ban_handler",
    "kick_handler"
]
