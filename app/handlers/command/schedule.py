from telegram import Update
from telegram.ext import ContextTypes

from app.settings import FILES_DIR
from app.handlers.bot import send_text, send_document
from app.src.db_days import get_today_schedule
from app.src.db_days import get_tomorrow_schedule
from app.src.db_days import get_schedule_for_this_week
from app.src.db_days import get_schedule_for_next_week
from app.templates import render_template


SINGLE_LESSON_TEMPLATE = "single.j2"
SCHEDULE_TEMPLATE = "schedule.j2"
SINGLE_VACATION_TEMPLATE = "single_vacation.j2"
THIS_WEEK_VACATIONS_TEMPLATE = "this_week_vacations.j2"
NEXT_WEEK_VACATIONS_TEMPLATE = "next_week_vacations.j2"


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    template = SINGLE_LESSON_TEMPLATE
    today_lesson = await get_today_schedule()
    if today_lesson is None:
        template = SINGLE_VACATION_TEMPLATE
        today_lesson = "Сегодня"

    if not update.message:
        return
    await send_text(
        update,
        context,
        render_template(
            template,
            {"lesson": today_lesson},
        ),
    )


async def tommorow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    template = SINGLE_LESSON_TEMPLATE
    tomorrow_lesson = await get_tomorrow_schedule()
    if tomorrow_lesson is None:
        template = SINGLE_VACATION_TEMPLATE
        tomorrow_lesson = "Завтра"

    if not update.message:
        return
    await send_text(
        update,
        context,
        render_template(
            template,
            {"lesson": tomorrow_lesson},
        ),
    )


async def this_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    template = SCHEDULE_TEMPLATE
    this_week_lessons = list(await get_schedule_for_this_week())
    if this_week_lessons == []:
        template = THIS_WEEK_VACATIONS_TEMPLATE

    if not update.message:
        return
    await send_text(
        update,
        context,
        render_template(
            template,
            {"lessons": this_week_lessons},
        ),
    )


async def next_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    template = SCHEDULE_TEMPLATE
    next_week_lessons = list(await get_schedule_for_next_week())
    if next_week_lessons == []:
        template = NEXT_WEEK_VACATIONS_TEMPLATE

    if not update.message:
        return
    await send_text(
        update,
        context,
        render_template(
            template,
            {"lessons": next_week_lessons},
        ),
    )


async def full_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    document = open(f"{FILES_DIR}/schedule.pdf", "rb")

    if not update.message:
        return
    await send_document(update, context, "Расписание на весь семестр", document)
