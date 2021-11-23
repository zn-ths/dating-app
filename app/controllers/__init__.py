from app.data.models import T
from app.data.models import BaseModel
from app.data.repository import BaseRepository


class BaseController:
    model = BaseModel

    @classmethod
    def create(cls, name: str) -> T:
        return BaseRepository.create(cls.model, name)

    @classmethod
    def find_by_id(cls, _id: int) -> T:
        return BaseRepository.find_by_id(cls.model, _id)

    @classmethod
    def find_by_name(cls, name: str) -> T:
        return BaseRepository.find_by_name(cls.model, name)

    @classmethod
    def find_all(cls) -> list[T]:
        return BaseRepository.find_all(cls.model)

    @classmethod
    def find_all_by_name(cls, name: str) -> list[T]:
        return BaseRepository.find_all_by_name(cls.model, name)

    @classmethod
    def update_one_by_name(cls, new_name: str) -> None:
        pass

    @classmethod
    def update_many_by_name(cls, new_name: str, old_name: str = None) -> None:
        # if none, update all, else update all by type?
        pass

    @classmethod
    def delete_by_id(cls, _id: int) -> None:
        BaseRepository.delete_by_id(cls.model, _id)

    @classmethod
    def delete_all(cls) -> None:
        BaseRepository.delete_all(cls.model)
