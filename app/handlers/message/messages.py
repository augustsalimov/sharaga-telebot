from telegram import Update, error
from telegram.ext import ContextTypes
from pathlib import Path
import json

from app.config import ADMIN_USER_ID, FILES_DIR
from app.handlers.bot import send_text, send_sticker, get_chat_member
from app.handlers import today, tommorow, this_week, next_week, full_schedule, user_stat, user_of_day
from app.templates import render_template
from app.src.phrases import PHRASES, REPEATED, STICKS
from app.src.db_users import get_all_users
from app.src.db_phrases import get_phrase


async def main(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    original_text = message.text
    lower_text = original_text.lower()
    user_id = str(message.from_user.id)
    try:
        username = message.from_user.username
    except Exception:
        username = "NULL"
    first_name = message.from_user.first_name

    # temporary, to get a user id of users in chat
    path = Path(f"{FILES_DIR}/users.json")
    with open(path) as f:
        dict_ = json.load(f)
    try:
        dict_[user_id]
    except Exception:
        dict_[user_id] = {
            "Username": username, 
            "First name": first_name
        }
        with open(path, 'w') as f:
            json.dump(dict_, f, ensure_ascii=False)
    
    if lower_text.startswith("пиздюк"):
        if user_id == ADMIN_USER_ID:
            await admin(update, context, lower_text.split("пиздюк")[1])
            return
        else:
            await send_text(update, context, "От пиздюка слышу")

    if "пар" in lower_text:
        await commands(update, context, lower_text)

    if any(word in lower_text for word in ["гей", "пидор", "геям", "пидорам"]):
        await user_stat(update, context)
        return
    
    if "выбери пидора дня" in lower_text:
        await user_of_day(update, context)
        return
    
    if "аджарски" in lower_text:
        await send_text(
            update,
            context,
            render_template(
                "recipe.j2",
            ),
        )
        return

    for key in REPEATED:
        if key in original_text:
            phrase = await get_phrase(key)
            phrase = phrase[0].phrase
            for i in range(3):
                await send_text(update, context, phrase)
            return
        
    for key in PHRASES:
        if key in lower_text:
            phrase = await get_phrase(key)
            phrase = phrase[0].phrase
            phrase = phrase.split(";")
            for i in phrase:
                await send_text(update, context, i)
            return
        
    for key in STICKS:
        if key in lower_text:
            phrase = await get_phrase(key)
            sticker_id = phrase[0].phrase
            await send_sticker(update, context, sticker_id)

    if all(word in lower_text for word in ["меня", "сегодня"]):
        sticker_id = "CAACAgIAAx0CbHmS5AACATNj7mqGShm_DT7LTmxDQac1jd-m7gACeSgAAlTQIEtXt23OvdXsBC4E"
        await send_sticker(update, context, sticker_id)
    

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str) -> None:
    if "отметь всех" in text:
        try:
            users_list = []
            users = await get_all_users()
            
            for user in users:
                user_id = user.user_id
                user = await get_chat_member(update, context, user_id)
                if user.username is None:
                    user_name = f"<a href='tg://user?id={user_id}'>{user.first_name}</a>"
                else:
                    user_name = f"@{user.username}"
                users_list.append(user_name)

            await send_text(update, context, "Хорошо, Босс")

            await send_text(
                update,
                context,
                " ".join(i for i in users_list)
            )
        except error.BadRequest:
            await send_text(
                update,
                context,
                "Босс, некоторые пользователи не найдены"
            )
    elif "я опоздаю" in text:
        await send_text(update, context, "Не спешите, Босс")
    else:
        await send_text(update, context, "Да, Босс")


async def commands(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str) -> None:
    if "сегодня" in text:
        await today(update, context)
    elif "завтра" in text:
        await tommorow(update, context)
    elif "на этой неделе" in text:
        await this_week(update, context)
    elif "на следующей неделе" in text:
        await next_week(update, context)
    elif "весь семестр" in text:
        await full_schedule(update, context)
    else:
        await send_text(update, context, "Кто сказал пара?")
    return
