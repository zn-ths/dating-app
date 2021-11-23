from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.data.models import BaseModel


class Hobby(BaseModel):
    __tablename__ = "hobbies"
    __table_args__ = {"schema": "dating-db"}

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(length=45), nullable=False)

    def __init__(self, name: str) -> None:
        self.name = name
