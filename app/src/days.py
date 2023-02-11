from collections.abc import Iterable
from dataclasses import dataclass
from typing import LiteralString, cast

from app import config
from app.db_model import fetch_all
from app.src import mydatetime

@dataclass
class Day:
    id: int
    date: str
    l_s: str
    cab: str
    lecturer_name: str
    subject_name: str
    lecturer_id: int = None
    subject_id: int = None


async def get_today_info() -> Iterable[Day]:
    sql = f"""{_days_base_sql_request()}
            WHERE my_date = "{mydatetime.today()}" """
    days = await _get_days_from_db(sql)
    return days


async def get_schedule_for_this_week() -> Iterable[Day]:
    sql = f"""{_days_base_sql_request()}
            WHERE my_date >= "{mydatetime.today()}" 
            and my_date <= "2023-02-17" """
    days = await _get_days_from_db(sql)
    return days


'''async def get_today() -> Iterable[Day]:
    sql = f"""{_days_base_sql_request()}
              ORDER BY d."my_date" """
    days = await _get_days_from_db(sql)
    return _dict_days_by_datetime_key(days)'''


def _days_base_sql_request(select_param: LiteralString | None = None) -> LiteralString:
    return f"""
        SELECT
            d.id as id,
            d.my_date as my_date,
            d.l_s as l_s,
            d.cab as cab,
            l.name as lecturer_name,
            s.name as subject_name
        FROM day d
        LEFT JOIN lecturer l ON d.lecturer_id  = l.id
        RIGHT JOIN subject s ON d.subject_id  = s.id
    """


async def _get_days_from_db(sql: LiteralString) -> list[Day]:
    day_raw = await fetch_all(sql)
    return [
        Day(
            id = day["id"],
            date = day["my_date"],
            l_s = day["l_s"],
            cab = day["cab"],
            lecturer_name = day["lecturer_name"],
            subject_name = day["subject_name"]
        )
        for day in day_raw
    ]
