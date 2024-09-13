from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..models import DBAchievement, DBMember, DBPayment
from ..schema import Achievement, Member, Payment
from ..services.member_service import (
    get_db_member_achivements,
    get_db_member_by_id,
    get_db_member_payments,
    get_db_members,
)
from .dependancies import get_session

router = APIRouter()


PROJECT_ROO = Path(__file__).parent.parent


@router.get("/", response_model=list[Member])
def get_all_members(db: Annotated[Session, Depends(get_session)]) -> list[DBMember]:
    return get_db_members(db)


@router.get("/{id}", response_model=Member)
def get_meber_by_id(id: int, db: Annotated[Session, Depends(get_session)]) -> DBMember:
    member = get_db_member_by_id(id, db)
    if member is None:
        raise HTTPException(
            status_code=404, detail=f"No Member with the id {id} found."
        )
    return member


@router.get("/{id}/achievements", response_model=list[Achievement])
def get_member_achievements(
    id: int, db: Annotated[Session, Depends(get_session)]
) -> list[DBAchievement]:
    achievenets: list[Achievement] = get_db_member_achivements(id, db)
    if achievenets is None:
        raise HTTPException(
            status_code=404,
            detail=f"No Achievements for members with the id {id} found.",
        )
    return achievenets


@router.get("/{id}/payments", response_model=list[Payment])
def get_member_payments(
    id: int, db: Annotated[Session, Depends(get_session)]
) -> list[DBPayment]:
    payments: list[Payment] = get_db_member_payments(id, db)
    if payments is None:
        raise HTTPException(
            status_code=404, detail=f"No Payments for members with the id {id} found."
        )
    return payments
