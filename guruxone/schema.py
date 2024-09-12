from datetime import date

from pydantic import BaseModel


class Member(BaseModel):
    id: int
    firstName: str
    lastName: str
    phoneNumber: str
    email: str
    dateofBirth: date
    # achievments:list
