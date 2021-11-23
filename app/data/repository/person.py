from app.data.db import session
from app.data.models.person import Person
from app.data.repository import BaseRepository


class PersonRepository(BaseRepository):
    @staticmethod
    def create(**kwargs) -> Person:
        kwargs["gender_id"] = kwargs["gender_id"].value
        person = Person(**kwargs)
        session.add(person)
        session.commit()
        return person

    # @staticmethod
    # def find_by_id(_id: int) -> Person:
    #     return session.query(Person).filter_by(id=_id).first()

    @staticmethod
    def find_all_by_age(age: int) -> list[Person]:
        pass

    @staticmethod
    def find_all_by_age_in_range(start: int = None, end: int = None) -> list[Person]:
        if not start and not end:
            pass
        elif start and not end:
            pass
        elif not start and end:
            pass
        else:
            pass

    @staticmethod
    def find_all_by_name_pattern(pattern: str,
                                 sensitive: bool = True,
                                 prefixed: bool = False,
                                 suffixed: bool = False) -> list[Person]:
        """

        By default checks if the name contains the pattern when
        prefixed or suffixed is not set to True.

        """

        # use String Template
        if prefixed:
            search = f"%{pattern}"
        elif suffixed:
            search = f"{pattern}%"
        else:
            search = f"%{pattern}%"

        if sensitive:
            return session.query(Person).filter(
                Person.customerName.like(search)).all()

        return session.query(Person).filter(
            Person.customerName.ilike(search)).all()

    @staticmethod
    def find_all_with_children(children: int = 0) -> list[Person]:
        if not children:
            # not specified, all children > 0
            pass
        # all with amount of children == children
        pass

    @staticmethod
    def find_all_without_children() -> list[Person]:
        pass
