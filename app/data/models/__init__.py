from typing import Generic
from typing import Type
from typing import TypeVar

from app.data.db import Base
from app.data.db import session


T = TypeVar("T", bound="BaseModel")


class BaseModel(Base, Generic[T]):
    __abstract__ = True

    def __repr__(self) -> str:
        attributes = ", ".join(f"{k}={v}" for k, v in self.to_dict().items())
        return f"{self.__class__.__name__}({attributes})"

    def __str__(self) -> str:
        attributes = "\n".join(f"\t{k}: {v}" for k, v in self.to_dict().items())
        return f"{self.__class__.__name__}:\n{attributes}"

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if k != "_sa_instance_state"}

    @classmethod
    def find_by_id(cls: Type[T], _id: int) -> T:
        return session.query(cls).filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls: Type[T], name: str) -> T:
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> list[T]:
        return session.query(cls).all()

    @classmethod
    def all_to_dict(cls, items: list[T] = None) -> list[dict]:
        return [item.to_dict() for item in (items if items else cls.find_all())]
