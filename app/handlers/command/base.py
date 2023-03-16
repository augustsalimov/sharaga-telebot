from telegram import Update
from telegram.ext import ContextTypes

from handlers.bot import send_text
from core import render_template


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_text(update, context, response=render_template("start.j2"))


async def commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_text(update, context, response=render_template("commands.j2"))


async def version(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_text(update, context, response=render_template("version.j2"))
