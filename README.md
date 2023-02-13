# SharagaNouBOT
Telegram-бот для группы.

## Инструменты
- Python 3.11
- Python-telegram-bot
- Aiosqlite
- Jinja2

## Команды
- /start - приветственное сообщение
- /commands - комманды
- /version - версия бота
- /links - все важные ссылки
- /contacts - контакты
- /today - какая сегодня пара
- /tomorrow - какая завтра пара
- /this_week - расписание на эту, оставшуюся часть недели
- /next_week - расписание на следующую неделю 
- /whole_schedule - файл со всем расписанием
- /mqu - мгу
- /russia - russia
- /recipe - рецепт<br>

## Запуск
Для начала, надо дать права скрипту `chmod +x init.sh` и запустить его `./init.sh` <br>
Заполнить появившийся `.env` файл <br>
Залить базу данных `cat app/db.sql | sqlite3 app/db.sqlite3` <br>
Затем можно запустить бота `poetry run python -m app` <br>

## Идеи
/deadlines - ближайшие дедлайны <br>
/pi*or - пи*ор дня <br>
Ответы на фразы <br>
Если сегодня нет пары, то указать ближайшую

## Тех бэклог
R&D - автоматизировать процесс скачки файла с расписанием <br>
парсинг файла и запись в бд <br>
докер <br>
ci/cd <br>
тесты <br>
pre-commit <br>
на серваке перейти со screen-а на systemd-юнит <br>
