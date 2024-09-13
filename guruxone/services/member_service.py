from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import DBAchievement, DBMember, DBPayment


def get_db_members(db: Session) -> list[DBMember]:
    return db.execute(select(DBMember)).scalars()


def get_db_member_by_id(id: int, db: Session) -> DBMember:
    return db.get(DBMember, id)


def get_db_member_achivements(id: int, db: Session) -> list[DBAchievement]:
    member = db.get(DBMember, id)
    if member is not None:
        return db.get(DBMember, id).achievements
    else:
        return []


def get_db_member_payments(id: int, db: Session) -> list[DBPayment]:
    member = db.get(DBMember, id)
    if member is not None:
        return db.get(DBMember, id).payments
    else:
        return []
