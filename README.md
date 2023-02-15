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
- /today - какая сегодня пара
- /tomorrow - какая завтра пара
- /this_week - расписание на эту, оставшуюся часть недели
- /next_week - расписание на следующую неделю 
- /full_schedule - файл со всем расписанием
- /links - все важные ссылки
- /contacts - контакты
- /user_of_day - пользователь дня
- /user_stat - статистика за месяц<br>
<br>
Еще бот отвечает на разные сообщения.

## Запуск
Для начала, надо дать права скрипту `chmod +x init.sh` и запустить его `./init.sh`<br>
Заполнить появившийся `.env` файл<br>
Залить базу данных `cat app/db.sql | sqlite3 app/db.sqlite3`<br>
Затем можно запустить бота `poetry run python -m app`<br>

## Идеи
/deadlines - ближайшие дедлайны<br>
Поменять формат вывода даты<br>
Если сегодня нет пары, то указать ближайшую<br>
Мемы<br>
R&D - админка из чата<br>

## Тех бэклог
R&D - автоматизировать процесс скачки файла с расписанием<br>
парсинг файла и запись в бд<br>
maintenance mode<br>
докер<br>
ci/cd<br>
тесты<br>
pre-commit<br>
на серваке перейти со screen-а на systemd-юнит<br>
