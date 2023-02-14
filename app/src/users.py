from collections.abc import Iterable
from dataclasses import dataclass

from app.db_model import fetch_all, execute
from app.src import mydatetime


@dataclass
class User:
    id: int
    user_id: str


async def get_all_users() -> Iterable[User]:
    sql = f"""{_all_users_base_sql_request()}"""
    days = await _get_users_from_db(sql)
    return days


def _all_users_base_sql_request() -> str:
    return """SELECT * FROM users"""


async def _get_users_from_db(sql: str) -> Iterable[User]:
    user_raw = await fetch_all(sql)
    return [
        User(
            id = user["id"],
            user_id = user["user_id"],
        )
        for user in user_raw
    ]


@dataclass
class UserDay:
    id: int
    date: str
    user_id: str


async def get_todays_user() -> Iterable[UserDay]:
    sql = f"""{_user_days_base_sql_request()}
        WHERE m.my_date = "{mydatetime.today()}" """
    user = await _get_user_days_from_db(sql)
    return user


async def write_todays_user(id: int) -> Iterable[UserDay]:
    sql = f"""
        INSERT INTO month (my_date, user) 
        VALUES ("{mydatetime.today()}", {id}) """
    await execute(sql)


async def get_champions() -> Iterable[UserDay]:
    sql = f"""{_user_days_base_sql_request()}
        WHERE my_date >= "{mydatetime.first_day_of_month()}" 
        and my_date <= "{mydatetime.last_day_of_month()}" 
        GROUP BY user_id
        ORDER BY user_id DESC
        LIMIT 10 
    """
    user = await _get_user_days_from_db(sql)
    return user


async def get_quantity(user_id: str) -> int:
    sql = f"""
        SELECT
            m.my_date as my_date,
            u.user_id as user_id,
            COUNT(u.user_id)
        FROM month m
        JOIN users u ON m.user = u.id
        WHERE user_id = "{user_id}" and my_date >= "{mydatetime.first_day_of_month()}" 
        and my_date <= "{mydatetime.last_day_of_month()}"
    """
    quantity = await _get_quantity_from_db(sql)
    return quantity


def _user_days_base_sql_request() -> str:
    return """
        SELECT
            m.id as id,
            m.my_date as my_date,
            u.user_id as user_id
        FROM month m
        JOIN users u ON m.user = u.id
    """


async def _get_quantity_from_db(sql: str) -> int:
    quantity_raw = await fetch_all(sql)
    return quantity_raw[0]['COUNT(u.user_id)']


async def _get_user_days_from_db(sql: str) -> Iterable[UserDay]:
    user_day_raw = await fetch_all(sql)
    return [
        UserDay(
            id = user_day["id"],
            date = user_day["my_date"],
            user_id = user_day["user_id"],
        )
        for user_day in user_day_raw
    ]
