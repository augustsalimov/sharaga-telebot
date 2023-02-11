from datetime import datetime, timedelta
from collections.abc import Iterable
import pytz


def timenow() -> datetime:
    return datetime.now(pytz.timezone('Europe/Moscow'))


def today() -> str:
    return _typer(timenow())


def weekday() -> str:
    return timenow().weekday() + 1


def this_week_dates() -> Iterable[str]:
    days_left_in_week = 7 - weekday()
    return [_typer(datetime.now() + timedelta(days=i)) for i in range(days_left_in_week)]


def sunday_date() -> str:
    days_left_in_week = 7 - weekday()
    return _typer(timenow() + timedelta(days=days_left_in_week))


def _typer(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")
