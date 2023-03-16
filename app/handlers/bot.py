import io
import telegram

from typing import cast
from telegram import Chat, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from core.settings import bot_settings


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
    if keyboard:
        args["reply_markup"] = keyboard

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
            text,
        )
    args = {"chat_id": _get_chat_id(update), "document": document}
    if keyboard:
        args["reply_markup"] = keyboard

    await context.bot.send_document(**args)


async def send_sticker(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    sticker_id: str,
    keyboard: InlineKeyboardMarkup | None = None,
) -> None:
    args = {
        "chat_id": _get_chat_id(update),
        "sticker": sticker_id,
    }
    if keyboard:
        args["reply_markup"] = keyboard

    await context.bot.send_sticker(**args)


async def get_chat_member(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    user_id: int,
) -> telegram.ChatMember:
    user = await context.bot.get_chat_member(
        chat_id=_get_chat_id(update),
        user_id=user_id,
    )

    return user.user


async def get_chat_members(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> telegram.ChatMember:
    chat = await context.bot.get_chat(
        chat_id=_get_chat_id(update),
    )

    return chat


async def is_group(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> bool:
    chat_members_count = await context.bot.get_chat_member_count(
        chat_id=_get_chat_id(update),
    )

    return True if chat_members_count > 2 else False


async def is_required_group(
    update: Update,
) -> bool:
    return True if str(_get_chat_id(update)) == str(bot_settings.CHAT_ID) else False


async def only_required_group_text(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await send_text(
        update,
        context,
        "Данная комманда доступна только в чате 425 группы",
    )


def _get_chat_id(update: Update) -> int:
    return cast(Chat, update.effective_chat).id
