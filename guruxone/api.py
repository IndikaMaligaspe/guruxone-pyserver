"""
api.py
___

The REST API for guruxone-api
"""

from pathlib import Path
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import DBAchievement, DBMember
from .schema import Achievement, Member
from .services.member_service import (
    get_db_member_achivements,
    get_db_member_by_id,
    get_db_members,
)

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
    return get_db_members(db)


@app.get("/member/{id}", response_model=Member)
def get_meber_by_id(id: int, db: Annotated[Session, Depends(get_session)]) -> DBMember:
    member = get_db_member_by_id(id, db)
    if member is None:
        raise HTTPException(
            status_code=404, detail=f"No Member with the id {id} found."
        )
    return member


@app.get("/member/{id}/achievements", response_model=list[Achievement])
def get_member_achievements(
    id: int, db: Annotated[Session, Depends(get_session)]
) -> list[DBAchievement]:
    achievenets = get_db_member_achivements(id, db)
    if achievenets is None or len(achievenets) == 0:
        raise HTTPException(
            status_code=404, detail=f"No Achievements for with the id {id} found."
        )
    return achievenets
