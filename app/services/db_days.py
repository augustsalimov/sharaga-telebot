from collections.abc import Iterable
from dataclasses import dataclass

from db_model import fetch_all
from services import mydatetime


@dataclass
class Day:
    id: int
    date: str
    l_s: str
    cab: str
    lecturer_name: str
    subject_name: str


async def get_today_schedule() -> Day | None:
    sql = f"""{_days_base_sql_request()}
            WHERE my_date = "{mydatetime.today()}" """
    days = await _get_days_from_db(sql)
    try:
        return days[0]
    except IndexError:
        return None


async def get_tomorrow_schedule() -> Day | None:
    sql = f"""{_days_base_sql_request()}
            WHERE my_date = "{mydatetime.tomorrow()}" """
    days = await _get_days_from_db(sql)
    try:
        return days[0]
    except IndexError:
        return None


async def get_schedule_for_this_week() -> Iterable[Day]:
    sql = f"""{_days_base_sql_request()}
            WHERE my_date >= "{mydatetime.today()}" 
            and my_date <= "{mydatetime.sunday_date()}" """
    days = await _get_days_from_db(sql)
    return days


async def get_schedule_for_next_week() -> Iterable[Day]:
    sql = f"""{_days_base_sql_request()}
            WHERE my_date >= "{mydatetime.next_monday_date()}" 
            and my_date <= "{mydatetime.next_sunday_date()}" """
    days = await _get_days_from_db(sql)
    return days


def _days_base_sql_request() -> str:
    return """
        SELECT
            d.id as id,
            d.my_date as my_date,
            d.l_s as l_s,
            d.cab as cab,
            l.name as lecturer_name,
            s.name as subject_name
        FROM schedule d
        LEFT JOIN lecturer l ON d.lecturer_id  = l.id
        RIGHT JOIN subject s ON d.subject_id  = s.id
    """


async def _get_days_from_db(sql: str) -> Iterable[Day]:
    day_raw = await fetch_all(sql)
    return [
        Day(
            id=day["id"],
            date="-".join(day["my_date"].split("-")[::-1]),
            l_s=day["l_s"],
            cab=day["cab"],
            lecturer_name=day["lecturer_name"],
            subject_name=day["subject_name"],
        )
        for day in day_raw
    ]
