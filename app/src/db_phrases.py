from collections.abc import Iterable
from dataclasses import dataclass

from app.db_model import fetch_all


@dataclass
class Phrase:
    id: int
    key_phrase: str
    phrase: str


async def get_phrase(key_phrase: str) -> Iterable[Phrase]:
    sql = f"""{_phrases_base_sql_request()}
            WHERE key_phrase = "{key_phrase}" """
    phrase = await _get_phrases_from_db(sql)
    return phrase


def _phrases_base_sql_request() -> str:
    return """SELECT * FROM phrases"""


async def _get_phrases_from_db(sql: str) -> Iterable[Phrase]:
    phrase_raw = await fetch_all(sql)
    return [
        Phrase(
            id=phrase["id"], key_phrase=phrase["key_phrase"], phrase=phrase["phrase"]
        )
        for phrase in phrase_raw
    ]


@dataclass
class UserPhrases:
    id: int
    phrase: str


async def get_all_phrases() -> Iterable[UserPhrases]:
    sql = f"""{_user_phrases_base_sql_request()}"""
    phrase = await _get_user_phrases_from_db(sql)
    return phrase


def _user_phrases_base_sql_request() -> str:
    return """SELECT * FROM user_phrases"""


async def _get_user_phrases_from_db(sql: str) -> Iterable[UserPhrases]:
    phrase_raw = await fetch_all(sql)
    return [
        UserPhrases(id=phrase["id"], phrase=phrase["phrase"]) for phrase in phrase_raw
    ]
