from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

import handlers
from core import bot_settings, logger
from db_model import close_db


COMMAND_HANDLERS = {
    "start": handlers.start,
    "commands": handlers.commands,
    "today": handlers.today,
    "tomorrow": handlers.tommorow,
    "this_week": handlers.this_week,
    "next_week": handlers.next_week,
    "full_schedule": handlers.full_schedule,
    "links": handlers.links,
    "contacts": handlers.contacts,
    "user_of_day": handlers.user_of_day,
    "user_stat": handlers.user_stat,
}


if not bot_settings.TELEGRAM_BOT_TOKEN:
    # or not bot_settings.TELEGRAM_BOT_CHANNEL_ID:
    raise ValueError("env variables wasn't implemented")


def main() -> None:
    application = ApplicationBuilder().token(bot_settings.TELEGRAM_BOT_TOKEN).build()

    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))

    application.add_handler(
        MessageHandler(
            filters.TEXT & (~filters.Sticker.ALL & ~filters.COMMAND), handlers.main
        )
    )

    application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
    finally:
        close_db()
