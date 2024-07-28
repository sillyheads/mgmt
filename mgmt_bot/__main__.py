from .bot import bot_main
import logging

logging.basicConfig(
    level=logging.WARNING,
    filename='app.log'
)

bot_main()
