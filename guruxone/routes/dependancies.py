from sqlalchemy.orm import Session

from ..database import SessionLocal


def get_session() -> Session:  # type: ignore
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
