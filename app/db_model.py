import asyncio
from collections.abc import Iterable
from typing import Any

import aiosqlite

from core import SQLITE_DB_FILE


async def get_db() -> aiosqlite.Connection:
    if not getattr(get_db, "db", None):
        db = await aiosqlite.connect(SQLITE_DB_FILE)
        get_db.db = db

    return get_db.db


async def fetch_all(sql: str, params: Iterable[Any] | None = None) -> list[dict]:
    cursor = await _get_cursor(sql, params)
    rows = await cursor.fetchall()
    results = []
    for row_ in rows:
        results.append(_get_result_with_column_names(cursor, row_))
    await cursor.close()

    return results


async def execute(
    sql: str, params: Iterable[Any] | None = None, *, autocommit: bool = True
) -> None:
    db = await get_db()
    args: tuple[str, Iterable[Any] | None] = (sql, params)
    await db.execute(*args)
    if autocommit:
        await db.commit()


def close_db():
    asyncio.run(_async_close_db())


async def _async_close_db():
    await (await get_db()).close()


async def _get_cursor(sql: str, params: Iterable[Any] | None) -> aiosqlite.Cursor:
    db = await get_db()
    args: tuple[str, Iterable[Any] | None] = (sql, params)
    cursor = await db.execute(*args)
    db.row_factory = aiosqlite.Row

    return cursor


def _get_result_with_column_names(cursor: aiosqlite.Cursor, row: aiosqlite.Row) -> dict:
    column_names = [d[0] for d in cursor.description]
    resulting_row = {}
    for index, column_name in enumerate(column_names):
        resulting_row[column_name] = row[index]

    return resulting_row
