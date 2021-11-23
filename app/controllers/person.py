# from datetime import date

from app.controllers import BaseController
from app.data.models.person import Person
from app.data.repository.person import PersonRepository


class PersonController(BaseController):
    model = Person

    @staticmethod
    def create(**kwargs) -> Person:
        return PersonRepository.create(**kwargs)

    # @classmethod
    # def create(cls,
    #            name: str,
    #            surname: str,
    #            birthday: date,
    #            have_children: bool,
    #            street_address: str,
    #            zip_code: str,
    #            city: str,
    #            country: str,
    #            phone_number: str,
    #            email: str,
    #            gender_id: int) -> Person:
    #     return PersonRepository.create(
    #         name=name,
    #         surname=surname,
    #         birthday=birthday,
    #         have_children=have_children,
    #         street_address=street_address,
    #         zip_code=zip_code,
    #         city=city,
    #         country=country,
    #         phone_number=phone_number,
    #         email=email,
    #         gender_id=gender_id)

    # @staticmethod
    # def find_by_id(_id: int) -> Person:
    #     return PersonRepository.find_by_id(_id)

    @staticmethod
    def find_by_first_name(first_name: str) -> Person:
        pass

    @staticmethod
    def find_by_last_name(last_name: str) -> Person:
        pass

    @staticmethod
    def find_by_full_name(full_name: str) -> Person:
        pass

    @staticmethod
    def find_by_pattern(pattern: str) -> Person:
        pass

    @staticmethod
    def update():
        pass
