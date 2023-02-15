from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.bot import send_text, send_sticker
from app.templates import render_template
from app.src.phrases import PHRASES, STICKS


async def phrases(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if "хачапури по-аджарски" in update.message.text:
        await send_text(
            update,
            context,
            render_template(
                "recipe.j2",
            ),
        )
        return
    
    for key, value in PHRASES.items():
        if key in update.message.text:
            if type(value) == list:
                for val in value: 
                    await send_text(update, context, val)
                return
            for i in range(3):
                await send_text(update, context, value)
            return

    for key, value in STICKS.items():
        if key in update.message.text:
            await send_sticker(update, context, value)
