import secrets
from telegram import Update
from telegram import error
from telegram.ext import ContextTypes

from app.handlers.bot import send_text, get_chat_member
from app.handlers.bot import is_required_group, only_required_group_text
from app.src.db_users import get_all_users, get_todays_user, write_todays_user
from app.src.db_users import get_champions, get_quantity
from app.src.db_phrases import get_all_phrases
from app.templates import render_template


async def user_of_day(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await is_required_group(update):
        try:
            list(await get_todays_user())[0]
            await send_text(
                update,
                context,
                "Сегодня выбор уже сделан"
            )

        except IndexError:
            users = list(await get_all_users())
            
            user = secrets.choice(users)
            id = user.id
            user_id = user.user_id
            try:
                user = await get_chat_member(update, context, user_id)
                if user.username is None:
                    user_name = f"<a href='tg://user?id={user_id}'>{user.first_name}</a>"
                else:
                    user_name = f"@{user.username}"

                await write_todays_user(id)

                if not update.message: return

                phrases = secrets.choice(list(await get_all_phrases()))
                phrases = phrases.phrase.split(";")
                for phrase in phrases:
                    await send_text(
                        update,
                        context,
                        phrase
                    )

                await send_text(
                    update,
                    context,
                    f"{user_name} пиdор дня"
                )
            except error.BadRequest:
                await send_text(
                    update,
                    context,
                    "Пользователь не найден",
                )
    else:
        await only_required_group_text(update, context)


async def user_stat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await is_required_group(update):
        template = "champions.j2"

        list_of_champions = list(await get_champions())
        if list_of_champions == []:
            await send_text(
                update,
                context,
                "Пока статистика пуста"
            )
            return
        else:
            out_list = []
            for i, champion in enumerate(list_of_champions, start=1):
                user_id = champion.user_id
                user = await get_chat_member(update, context, user_id)

                out_list.append((
                    i, 
                    user.first_name, 
                    await get_quantity(user_id)
                ))
            await send_text(
                    update,
                    context,
                    render_template(
                        template,
                        {"champions": out_list},
                    ),
                )
    else:
        await only_required_group_text(update, context)
