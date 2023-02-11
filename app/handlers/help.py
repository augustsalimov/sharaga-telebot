from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.response import send_response
from app.templates import render_template


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, response=render_template("help.j2"))
