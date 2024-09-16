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


def update_db_member(id: int, data: dict, db: Session) -> DBMember | None:
    member: DBMember = db.get(DBMember, id)
    if member is not None:
        for key, val in data.items():
            setattr(member, key, val) if val else None
        db.commit()
        member = db.get(DBMember, id)
        return member
    else:
        return None
