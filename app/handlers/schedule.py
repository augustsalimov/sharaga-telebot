from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.response import send_text, send_document
from app.src.days import get_today_schedule
from app.src.days import get_tomorrow_schedule
from app.src.days import get_schedule_for_this_week
from app.src.days import get_schedule_for_next_week
from app.templates import render_template


SINGLE_TEMPLATE = "single.j2"
SCHEDULE_TEMPLATE = "schedule.j2"
TODAY_VACATION_TEMPLATE = "today_vacation.j2"
TOMORROW_VACATION_TEMPLATE = "tomorrow_vacation.j2"
THIS_WEEK_VACATIONS_TEMPLATE = "this_week_vacations.j2"
NEXT_WEEK_VACATIONS_TEMPLATE = "next_week_vacations.j2"


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    template = SINGLE_TEMPLATE
    try:
        today_lesson = list(await get_today_schedule())[0]
    except:
        today_lesson = ""
        template = TODAY_VACATION_TEMPLATE

    if not update.message: return
    await send_text(
        update,
        context,
        render_template(
            template,
            {"lesson": today_lesson},
        ),
    )


async def tommorow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    template = SINGLE_TEMPLATE
    try:
        tomorrow_lesson = list(await get_tomorrow_schedule())[0]
    except:
        tomorrow_lesson = ""
        template = TOMORROW_VACATION_TEMPLATE
    if not update.message: return

    await send_text(
        update,
        context,
        render_template(
            template,
            {"lesson": tomorrow_lesson},
        ),
    )


async def this_week(update: Update, context: ContextTypes.DEFAULT_TYPE):
    this_week_lessons = list(await get_schedule_for_this_week())
    if this_week_lessons == []:
        template = THIS_WEEK_VACATIONS_TEMPLATE
    else:
        template = SCHEDULE_TEMPLATE
    if not update.message: return

    await send_text(
        update,
        context,
        render_template(
            template,
            {"lessons": this_week_lessons},
        ),
    )


async def next_week(update: Update, context: ContextTypes.DEFAULT_TYPE):
    next_week_lessons = list(await get_schedule_for_next_week())
    if next_week_lessons == []:
        template = NEXT_WEEK_VACATIONS_TEMPLATE
    else:
        template = SCHEDULE_TEMPLATE
    if not update.message: return

    await send_text(
        update,
        context,
        render_template(
            template,
            {"lessons": next_week_lessons},
        ),
    )


async def whole_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = open("app/files/schedule.pdf", "rb")

    if not update.message: return

    await send_document(
        update,
        context,
        "Расписание на весь семестр",
        document
    )
