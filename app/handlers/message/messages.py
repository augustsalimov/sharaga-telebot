from telegram import Update, error
from telegram.ext import ContextTypes

from core.settings import bot_settings
from handlers.bot import send_text, send_sticker, get_chat_member
from handlers import (
    today,
    tommorow,
    this_week,
    next_week,
    full_schedule,
    user_stat,
    user_of_day,
)
from core.templates import render_template
from services.phrases import PHRASES, REPEATED, STICKS
from services.db_users import get_all_users
from services.db_phrases import get_phrase


async def main(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    original_text = message.text
    lower_text = original_text.lower()
    user_id = str(message.from_user.id)

    if "пиздюк" in lower_text:
        if user_id == bot_settings.ADMIN_USER_ID:
            await admin(update, context, lower_text.split("пиздюк")[1])
        else:
            await send_text(update, context, "От пиздюка слышу")
        return

    if "пар" in lower_text:
        await schedule_commands(update, context, lower_text)
    if "пидор" in lower_text:
        await user_commands(update, context, lower_text)

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
            return

    if (
        all(word in lower_text for word in ["меня", "не будет"])
        or all(word in lower_text for word in ["сегодня", "не буду"])
        or "не приеду" in lower_text
    ):
        sticker_id = "CAACAgIAAx0CbHmS5AACATNj7mqGShm_DT7LTmxDQac1jd-m7gACeSgAAlTQIEtXt23OvdXsBC4E"
        await send_sticker(update, context, sticker_id)
        return


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str) -> None:
    if "отметь всех" in text:
        try:
            users_list = []
            users = await get_all_users()

            for user in users:
                user_id = user.user_id
                user = await get_chat_member(update, context, user_id)
                if user.username is None:
                    user_name = (
                        f"<a href='tg://user?id={user_id}'>{user.first_name}</a>"
                    )
                else:
                    user_name = f"@{user.username}"
                users_list.append(user_name)

            await send_text(update, context, "Хорошо, Босс")

            await send_text(update, context, " ".join(i for i in users_list))
        except error.BadRequest:
            await send_text(update, context, "Босс, некоторые пользователи не найдены")
    elif "опоздаю" in text:
        await send_text(update, context, "Не спешите, Босс")
    elif "позоришь" in text:
        await send_text(update, context, "Извините, Босс")
    else:
        await send_text(update, context, "Да, Босс")
    return


async def schedule_commands(
    update: Update, context: ContextTypes.DEFAULT_TYPE, text: str
) -> None:
    dict_ = {
        "сегодня": today,
        "завтра": tommorow,
        "на этой неделе": this_week,
        "на эту неделю": this_week,
        "на следующей неделе": next_week,
        "на следующую неделю": next_week,
        "весь семестр": full_schedule,
    }
    for key, val in dict_.items():
        if key in text:
            await val(update, context)
            return
    return


async def user_commands(
    update: Update, context: ContextTypes.DEFAULT_TYPE, text: str
) -> None:
    if "выбери" in text:
        await user_of_day(update, context)
        return
    await user_stat(update, context)
    return
