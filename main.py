from typing import Annotated, AsyncGenerator
from random import randint

from deta import AsyncBase as async_base
from deta._async.client import _AsyncBase as AsyncBase
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['GET'],
    allow_headers=['*'],
)


class Nonogram(BaseModel):
    catalogue: str
    title: str
    by: str
    copyright: str
    license: str
    height: int
    width: int
    rows: list[list[int]]
    columns: list[list[int]]
    goal: list[list[bool]]


async def nonogram_db() -> AsyncGenerator[AsyncBase, None]:
    base = async_base('nonograms')
    yield base
    await base.close()


@app.get('/')
async def list_nonograms(
    nonogram_db: Annotated[AsyncBase, Depends(nonogram_db)],
) -> list[str]:
    """List keys of available nonograms

    Returns:
        Keys of available nonograms.
    """
    nonograms = await nonogram_db.fetch()
    return [
        nonogram['key']
        for nonogram in nonograms.items
    ]


@app.get('/random')
async def get_random_nonogram(
    nonogram_db: Annotated[AsyncBase, Depends(nonogram_db)],
) -> Nonogram:
    """Get random nonogram.

    Returns:
        Random nonogram.
    """
    nonograms = await nonogram_db.fetch()
    nonogram = nonograms.items[randint(0, len(nonograms.items) - 1)]
    return Nonogram.model_validate(nonogram)


@app.get('/{key}')
async def get_nonogram(
    key: str,
    nonogram_db: Annotated[AsyncBase, Depends(nonogram_db)],
) -> Nonogram:
    """Get nonogram by key.

    Args:
        key: Nonogram key (title)

    Returns:
        Requested nonogram.
    """
    nonogram = await nonogram_db.get(key)
    if nonogram is None:
        raise HTTPException(status_code=404, detail='Nonogram not found')

    return Nonogram.model_validate(nonogram)
