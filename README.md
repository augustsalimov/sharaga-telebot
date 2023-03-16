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
Python 3.11, python-telegram-bot, sqlite, jinja2.<br>

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
These instructions will get you a copy of the project up and running on your local machine for development 
and testing purposes.<br> 
NOTE: instructions only for unix-like systems.

### Installing

First of all, install docker.<br>
Then clone this git repository `git clone git@github.com:augustsalimov/sharaga-telebot.git`.<br>
Give permissions to the bash scripts and run them.
```
chmod +x init.sh
chmod +x db.sh
sudo ./init.sh
sudo ./db.sh
```
Fill in `.env` file.<br>
Fill db with data.<br>

### Running
Now you can run it with `poetry run python -m app` command.

## TODO <a name="todo"></a>
/deadlines<br>
/user bugfix<br>
/user_stat after /user<br>
Next class if there are no class today<br>
Memes<br>
code refactoring<br><br>
R&D - automate proccess of downloading schedule file<br>
script for parsing of the file and writing it to the db<br>
maintenance mode<br>
ci/cd<br>
tests<br>
pre-commit<br>
systemd<br>
