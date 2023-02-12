# Telegram-бот для шараги
Telegram-бот для группы из шараги.

## Инструменты
- Python 3.11
- Python-telegram-bot
- Aiosqlite
- Jinja2

## Команды
- /start - приветственное сообщение
- /commands — комманды
- /version - версия бота
- /links — все важные ссылки
- /today - какая сегодня пара
- /tomorrow - какая завтра пара
- /this_week - расписание на эту, оставшуюся часть недели
- /next_week - расписание на следующую неделю 
- /whole_schedule - файл со всем расписанием
- /mqu<br>

## Запуск
Для начала, надо дать права скрипту `chmod +x init.sh` и запустить его `./init.sh` <br>
Заполнить появившийся `.env` файл <br>
Залить базу данных `cat app/db.sql | sqlite3 app/db.sqlite3` <br>
Затем можно запустить бота `poetry run python -m app` <br>

## Идеи
/contacts - контакты, почты <br>
/deadlines - ближайшие дедлайны <br>
/pi*or - пи*ор дня <br>
Приколяшки
R&D - автоматизировать процесс скачки файла с расписанием <br>
