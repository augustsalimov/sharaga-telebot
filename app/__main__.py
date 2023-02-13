import logging

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)

from app import config, handlers
from app.db_model import close_db


COMMAND_HANDLERS = {
    "start": handlers.start,
    "commands": handlers.commands,
    "version": handlers.version,
    "links": handlers.links,
    "contacts": handlers.contacts,
    "today": handlers.today,
    "tomorrow": handlers.tommorow,
    "this_week": handlers.this_week,
    "next_week": handlers.next_week,
    "whole_schedule": handlers.whole_schedule,
    "mqu": handlers.mqu,
    "russia": handlers.russia,
    "recipe": handlers.recipe,
}


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


if not config.TELEGRAM_BOT_TOKEN: # or not config.TELEGRAM_BOT_CHANNEL_ID:
    raise ValueError("env variables wasn't implemented")


def main():
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))

    application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
    finally:
        close_db()
