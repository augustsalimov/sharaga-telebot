from collections.abc import Iterable
from dataclasses import dataclass

from app.db_model import fetch_all


@dataclass
class Phrase:
    id: int
    phrase: str


async def get_all_phrases() -> Iterable[Phrase]:
    sql = f"""{_phrases_base_sql_request()}"""
    phrase = await _get_phrases_from_db(sql)
    return phrase


def _phrases_base_sql_request() -> str:
    return """SELECT * FROM phrases"""


async def _get_phrases_from_db(sql: str) -> Iterable[Phrase]:
    phrase_raw = await fetch_all(sql)
    return [
        Phrase(
            id = phrase["id"],
            phrase = phrase["phrase"]
        )
        for phrase in phrase_raw
    ]
