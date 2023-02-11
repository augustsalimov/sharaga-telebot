from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.response import send_response
from app.src.days import get_today_info
from app.templates import render_template


async def today_class(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today_class = ""
    template = "today_class.j2"
    try:
        today_class = list(await get_today_info())[0]
    except:
        template = "vacation.j2"

    if not update.message:
        return

    await send_response(
        update,
        context,
        render_template(
            template,
            {"today": today_class},
        ),
    )