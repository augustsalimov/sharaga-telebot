from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.response import send_text
# from app.templates import render_template


async def mqu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    template = [
        "Нихуя себе",
        "У нас есть бот",
        "Я обожаю наш вуз!!!",
        "МГУ сосатб!!!",
    ]
    for phrase in template:
        await send_text(update, context, response=phrase)
