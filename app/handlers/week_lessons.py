from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.response import send_response
from app.src.days import get_schedule_for_this_week
from app.templates import render_template


async def week_lessons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    this_week_lessons = list(await get_schedule_for_this_week())
    if this_week_lessons == []:
        template = "vacations.j2"
    else:
        template = "week_lessons.j2"

    if not update.message:
        return

    await send_response(
        update,
        context,
        render_template(
            template,
            {"lessons": this_week_lessons},
        ),
    )
