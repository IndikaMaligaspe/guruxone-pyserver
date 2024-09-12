"""
api.py
___

The REST API for guruxone-api
"""

from pathlib import Path
from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import DBMember
from .schema import Member

app = FastAPI()

PROJECT_ROO = Path(__file__).parent.parent


def get_session() -> Session:  # type: ignore
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/member", response_model=list[Member])
def get_all_members(db: Annotated[Session, Depends(get_session)]) -> list[DBMember]:
    return db.execute(select(DBMember)).scalars()
