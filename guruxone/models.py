from datetime import datetime

# from database import SessionLocal
from sqlalchemy import TIMESTAMP, Date, Double, ForeignKey, Integer, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declarative_base,
    mapped_column,
    relationship,
)

Base: DeclarativeBase = declarative_base()


class DBMember(Base):
    __tablename__ = "members"

    id = mapped_column(Integer, primary_key=True)
    firstName = mapped_column(String(50), nullable=False)
    lastName = mapped_column(String(50), nullable=False)
    email = mapped_column(String(100), nullable=True)
    phoneNumber = mapped_column(String(50), nullable=True)
    dateofBirth = mapped_column(Date, nullable=True)
    createdAt = mapped_column(TIMESTAMP, nullable=False, default=datetime.now)
    updatedAt = mapped_column(TIMESTAMP, nullable=False, default=datetime.now)
    achievements: Mapped[list["DBAchievement"]] = relationship(back_populates="members")
    payments: Mapped[list["DBPayment"]] = relationship(back_populates="members")


class DBAchievement(Base):
    __tablename__ = "achievements"
    id = mapped_column(Integer, primary_key=True)
    achievementType = mapped_column(String(100), nullable=False)
    description = mapped_column(String(200), nullable=False)
    awardedBy = mapped_column(String(100), nullable=False)
    venue = mapped_column(String(100), nullable=True)
    dateAwarded = mapped_column(Date, nullable=True)
    createdAt = mapped_column(TIMESTAMP, nullable=False, default=datetime.now)
    updatedAt = mapped_column(TIMESTAMP, nullable=False, default=datetime.now)
    memberid = mapped_column(Integer, ForeignKey("members.id"))
    members: Mapped["DBMember"] = relationship(back_populates="achievements")


class DBPayment(Base):
    __tablename__ = "payments"
    id = mapped_column(Integer, primary_key=True)
    amount = mapped_column(Double, nullable=False, default=0.00)
    description = mapped_column(String(200), nullable=False)
    paymentMethod = mapped_column(String(100), nullable=True)
    paymentDate = mapped_column(Date, nullable=True)
    createdAt = mapped_column(TIMESTAMP, nullable=False, default=datetime.now)
    updatedAt = mapped_column(TIMESTAMP, nullable=False, default=datetime.now)
    memberid = mapped_column(Integer, ForeignKey("members.id"))
    members: Mapped["DBMember"] = relationship(back_populates="payments")


class DBUser(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(200), nullable=False)
    email = mapped_column(String(100), nullable=True)
    passwordHash = mapped_column(Date, nullable=True)
    createdAt = mapped_column(TIMESTAMP, nullable=False, default=datetime.now)
    updatedAt = mapped_column(TIMESTAMP, nullable=False, default=datetime.now)


# session = SessionLocal()
# results = session.execute(select(DBMember)).scalars()
# print("\n".join(member.achievements[0].description for member in results))
