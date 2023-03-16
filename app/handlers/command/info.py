from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.bot import send_text
from app.src.db_lecturers import get_lecturers
from app.templates import render_template


async def links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_text(update, context, response=render_template("links.j2"))


async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lecturers = list(await get_lecturers())

    if not update.message:
        return
    await send_text(
        update,
        context,
        render_template(
            "contacts.j2",
            {"lecturers": lecturers},
        ),
    )
