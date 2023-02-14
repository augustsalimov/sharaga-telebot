from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.bot import send_text
from app.templates import render_template


async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_text(update, context, response=render_template("links.j2"))
