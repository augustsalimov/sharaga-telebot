from telegram import Update
from telegram.ext import ContextTypes
from pathlib import Path
import json

from app.handlers.bot import send_text, send_sticker
from app.handlers import today, tommorow, this_week, next_week
from app.templates import render_template
from app.src.phrases import PHRASES, STICKS, RUSSIA_MSU


async def main(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message

    path = Path("app/files/users.json")
    with open(path) as f:
        dict_ = json.load(f)
    try:
        dict_[str(message.from_user.id)]
    except Exception:
        try:
            username = message.from_user.username
        except:
            username = "None"
        dict_[str(message.from_user.id)] = {
            "Username": username, 
            "First name": message.from_user.first_name
        }
        with open(path, 'w') as f:
            json.dump(dict_, f, ensure_ascii=False)

    original_text = message.text
    lower_text = message.text.lower()

    if "сегодня" in lower_text and "пара" in lower_text:
        await today(update, context)
        return
    elif "завтра" in lower_text and "пара" in lower_text:
        await tommorow(update, context)
        return
    elif "на этой неделе" in lower_text and "пар" in lower_text:
        await this_week(update, context)
        return
    elif "на следующей неделе" in lower_text and "пар" in lower_text:
        await next_week(update, context)
        return

    if "по-аджарски" in lower_text or "по аджарски" in lower_text:
        await send_text(
            update,
            context,
            render_template(
                "recipe.j2",
            ),
        )
        return
    
    for key, value in RUSSIA_MSU.items():
        if key in original_text:
            if type(value) == list:
                for val in value: 
                    await send_text(update, context, val)
                return
            for i in range(3):
                await send_text(update, context, value)
            return
    
    for key, value in PHRASES.items():
        if key in lower_text:
            for val in value: 
                await send_text(update, context, val)
            return

    for key, value in STICKS.items():
        if key in update.message.text:
            await send_sticker(update, context, value)
