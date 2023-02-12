from typing import cast
import io

import telegram
from telegram import Chat, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


async def send_text(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    response: str,
    keyboard: InlineKeyboardMarkup | None = None,
) -> None:
    args = {
        "chat_id": _get_chat_id(update),
        "disable_web_page_preview": True,
        "text": response,
        "parse_mode": telegram.constants.ParseMode.HTML,
    }
    if keyboard: args["reply_markup"] = keyboard
    
    await context.bot.send_message(**args)


async def send_document(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    text: str | None = None,
    document: io.TextIOWrapper | None = None,
    keyboard: InlineKeyboardMarkup | None = None,
) -> None:
    
    if text is not None:
        await send_text(
            update,
            context,
            text
        )

    args = {
        "chat_id": _get_chat_id(update),
        "document": document
    }
    if keyboard: args["reply_markup"] = keyboard
    
    await context.bot.send_document(**args)


def _get_chat_id(update: Update) -> int:
    return cast(Chat, update.effective_chat).id
