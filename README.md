# SharagaNouBOT
[![status](https://img.shields.io/badge/status-active-success.svg?style=flat-square)](https://github.com/augustsalimov/sharaga-telebot) 
[![last commit](https://img.shields.io/github/last-commit/augustsalimov/sharaga-telebot?style=flat-square)](https://github.com/augustsalimov/sharaga-telebot/commits/develop)<br>
This is repo of python scripted telegram bot for local university group. Main purpose is to provide students with schedule, links and contacts. Also it has some other features like answering to messages.

## Table of Contents

- [Tech stack](#stack)
- [Commands](#commands)
- [Getting Started](#getting_started)
- [TODO](#todo)

## Tech stack <a name="stack"></a>
Python 3.11, python-telegram-bot, aiosqlite, jinja2, docker.<br>

## Commands <a name="commands"></a>
- `/start` - welcome message
- `/commands` - commands
- `/today` - today's classes
- `/tomorrow` - tomorrow's classes
- `/this_week` - schedule for this week
- `/next_week` - schedule for next week
- `/full_schedule` - file with full schedule
- `/links` - all important links
- `/contacts` - contacts
- `/user_of_day` - user of the day
- `/user_stat` - statistics<br>

## Getting Started <a name="getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing
First of all, install docker.<br>
Then clone this git repository `git clone git@github.com:augustsalimov/sharaga-telebot.git`.<br>
Create and fill in `.env` file.<br>
Create db with command `cat ./app/db.sql | sqlite3 ./app/db.sqlite3`.<br>
Fill db with data.<br>

### Running
Now you can run project with `docker-compose up --build -d` command.

## TODO <a name="todo"></a>
/deadlines<br>
/user bugfix<br>
Next class if there are no class today<br>
Memes<br><br>
code refactoring<br>
R&D - automate proccess of downloading schedule file<br>
script for parsing of the file and writing it to the db<br>
ci/cd<br>
