from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import DBAchievement, DBMember, DBPayment


def get_db_members(db: Session) -> list[DBMember]:
    return db.execute(select(DBMember)).scalars().all()


def get_db_member_by_id(id: int, db: Session) -> DBMember:
    return db.get(DBMember, id)


def get_db_member_achivements(id: int, db: Session) -> list[DBAchievement] | None:
    member = db.get(DBMember, id)
    if member is not None:
        return member.achievements
    else:
        return None


def get_db_member_payments(id: int, db: Session) -> list[DBPayment] | None:
    member = db.get(DBMember, id)
    if member is not None:
        return member.payments
    else:
        return None
