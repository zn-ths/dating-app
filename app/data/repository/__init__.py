from typing import Type
from typing import TypeVar

from app.data.db import session
from app.data.models import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseRepository:
    @staticmethod
    def create(model: Type[T], name: str) -> T:
        instance = model(name)
        session.add(instance)
        session.commit()
        return instance

    @staticmethod
    def find_by_id(model: Type[T], _id: int) -> T:
        return model.find_by_id(_id)

    @staticmethod
    def find_by_name(model: Type[T], name: str) -> T:
        return model.find_by_name(name)

    @staticmethod
    def find_all(model: Type[T]) -> list[T]:
        return model.find_all()

    @staticmethod
    def find_all_by_name(model: Type[T], name: str) -> list[T]:
        return session.query(model).filter_by(name=name).all()

    @staticmethod
    def delete_by_id(model: Type[T], _id: int) -> None:
        gender = model.find_by_id(_id)
        if gender:
            gender.delete_from_db()

    @staticmethod
    def delete_all(model: Type[T]) -> None:
        session.query(model).delete()
        session.commit()
