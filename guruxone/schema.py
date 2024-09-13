from datetime import date
from typing import Optional

from pydantic import BaseModel


class Member(BaseModel):
    id: int
    firstName: str
    lastName: str
    phoneNumber: str
    email: str
    dateofBirth: date


class Achievement(BaseModel):
    id: int
    achievementType: str
    description: Optional[str] = None
    awardedBy: str
    venue: Optional[str] = None
    dateAwarded: date


class Payment(BaseModel):
    id: int
    amount: float
    description: Optional[str] = None
    paymentMethod: str
    paymentDate: date
