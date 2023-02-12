from datetime import datetime, timedelta
from collections.abc import Iterable
import pytz


def this_week_dates() -> Iterable[str]:
    days_left_in_week = 7 - _weekday()
    return [_typer(datetime.now() + timedelta(days=i)) for i in range(days_left_in_week)]


def today() -> str:
    return _typer(_timenow())


def tomorrow() -> str:
    return _typer(_timenow() + timedelta(days=1))


def sunday_date() -> str:
    days_left_in_week = 7 - _weekday()
    return _typer(_timenow() + timedelta(days=days_left_in_week))


def next_monday_date() -> str:
    days_to_the_monday = 8 - _weekday()
    return _typer(_timenow() + timedelta(days=days_to_the_monday))


def next_sunday_date() -> str:
    days_to_the_next_sunday = 14 - _weekday()
    return _typer(_timenow() + timedelta(days=days_to_the_next_sunday))


def _weekday() -> str:
    return _timenow().weekday() + 1


def _timenow() -> datetime:
    return datetime.now(pytz.timezone('Europe/Moscow'))


def _typer(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")
