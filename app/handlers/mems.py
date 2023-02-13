from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.response import send_text
from app.templates import render_template


async def mqu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    template = [
        "Нихуя себе",
        "У нас есть бот",
        "Я обожаю наш вуз!!!",
        "МГУ сосатб!!!",
    ]
    for phrase in template:
        await send_text(update, context, response=phrase)


async def russia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    template = "РА СИ Я!!!"
    for i in range(4):
        await send_text(update, context, response=template)


async def recipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message: return
    await send_text(
        update,
        context,
        render_template(
            "recipe.j2",
        ),
    )
