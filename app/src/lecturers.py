from collections.abc import Iterable
from dataclasses import dataclass

from app.db_model import fetch_all


@dataclass
class Lecturer:
    id: int
    name: str
    email: str
    subject: str


async def get_lecturers() -> Iterable[Lecturer]:
    sql = f"""{_lecturers_base_sql_request()} """
    lecturers = await _get_lecturers_from_db(sql)
    return lecturers


async def _get_lecturers_from_db(sql: str) -> Iterable[Lecturer]:
    lecturers_raw = await fetch_all(sql)
    return [
        Lecturer(
            id = lecturer["lecturer_id"],
            name = lecturer["name"],
            email = lecturer["email"],
            subject = lecturer["subject_name"]
        )
        for lecturer in lecturers_raw
    ]


def _lecturers_base_sql_request() -> str:
    return """
        SELECT
            l.id as lecturer_id,
            l.name as name,
            l.e_mail as email,
            s.name as subject_name
        FROM subject s
        JOIN lecturer l ON s.lecturer_id = l.id
        GROUP BY l.name
    """
