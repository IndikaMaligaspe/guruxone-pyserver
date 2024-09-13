from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import DBMember


def get_db_members(db: Session) -> list[DBMember]:
    return db.execute(select(DBMember)).scalars()
