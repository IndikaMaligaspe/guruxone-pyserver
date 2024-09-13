from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import DBMember


def get_db_members(db: Session) -> list[DBMember]:
    return db.execute(select(DBMember)).scalars()


def get_db_member_by_id(id: int, db: Session) -> DBMember:
    return db.get(DBMember, id)
