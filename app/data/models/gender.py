from enum import Enum

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.data.models import BaseModel


class Gender(BaseModel):
    __tablename__ = "gender"
    __table_args__ = {"schema": "dating-db"}

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(length=25), nullable=False)

    def __init__(self, name: str) -> None:
        self.name = name


class GenderType(Enum):
    FEMALE = 1
    MALE = 2
    OTHER = 3
