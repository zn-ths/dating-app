from __future__ import annotations
import datetime
import random

from app.controllers.person import PersonController
from app.data.models.gender import GenderType
from shared.utils.files import read_in_data_from_json_file
from shared.utils.files import read_in_data_from_text_file
from shared.utils.timer import timer


class PersonGenerator:
    EMAIL_HOSTS = ["gmail.com", "hotmail.com", "outlook.com", "live.se", "yahoo.com"]
    FEMALE_NAMES = []
    MALE_NAMES = []
    OTHER_NAMES = []
    LAST_NAMES = []
    PHONE_NUMBERS = []
    LOCATIONS = []

    @staticmethod
    def generate(**kwargs: dict) -> None:
        PersonController.create(**kwargs)

    @staticmethod
    def random_item(items: list) -> str | dict:
        return random.choice(items)

    @staticmethod
    def generate_email(first_name: str, last_name: str) -> str:
        return f"{first_name.lower()}.{last_name.lower()}@" \
               f"{random.choice(PersonGenerator.EMAIL_HOSTS)}"

    @staticmethod
    def random_birthday(start_date: str, end_date: str) -> datetime.date:
        """
        Generates a random date between start_date and end_date
        :param start_date: str in format YYYY-mm-dd
        :param end_date: str in format YYYY-mm-dd
        :return: datetime.date()
        """

        if len(start_date.split("-")) != 3 or len(end_date.split("-")) != 3:
            raise ValueError("Dates must be a str given in the format YYYY-mm-dd.")

        start_year, start_month, start_day = start_date.split("-")
        end_year, end_month, end_day = end_date.split("-")
        for digit in [start_year, start_month, start_day, end_year, end_month, end_day]:
            if not digit.isdigit():
                raise ValueError("Dates must be a str given in the format YYYY-mm-dd.")

        start_date = datetime.date(int(start_year), int(start_month), int(start_day))
        end_date = datetime.date(int(end_year), int(end_month), int(end_day))

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_numbers_of_days = random.randrange(days_between_dates)
        return start_date + datetime.timedelta(days=random_numbers_of_days)

    @staticmethod
    def process_street_no(street_no: str) -> str:
        start, end = [int(num) for num in street_no.split(" - ")]
        return str(random.randrange(start, end))

    @staticmethod
    def generate_random_person(gender: str) -> dict:
        person = {}

        if gender == "other":
            person["name"] = PersonGenerator.random_item(PersonGenerator.OTHER_NAMES)
            person["gender_id"] = GenderType.OTHER
        elif gender == "female":
            person["name"] = PersonGenerator.random_item(PersonGenerator.FEMALE_NAMES)
            person["gender_id"] = GenderType.FEMALE
        else:
            person["name"] = PersonGenerator.random_item(PersonGenerator.MALE_NAMES)
            person["gender_id"] = GenderType.MALE

        person["surname"] = PersonGenerator.random_item(PersonGenerator.LAST_NAMES)
        person["birthday"] = PersonGenerator.random_birthday("1921-01-01", "2002-12-31")
        person["have_children"] = random.choice([True, False, None])

        locus: dict = PersonGenerator.random_item(PersonGenerator.LOCATIONS)
        try:
            street_no = PersonGenerator.process_street_no(locus['street_no'])
        except (KeyError, ValueError):
            street_no = random.randrange(1, 99)

        person["street_address"] = f"{locus['street_address']} {street_no}"
        person["zip_code"] = locus["zip_code"]
        person["city"] = locus["city"]

        person["country"] = "Sweden"
        person["phone_number"] = PersonGenerator.random_item(PersonGenerator.PHONE_NUMBERS)
        person["email"] = PersonGenerator.generate_email(person["name"], person["surname"])

        return person

    @staticmethod
    @timer
    def generate_data_for_db(generations: int) -> None:
        PersonGenerator.read_in_all_data()

        for _ in range(generations):
            if (gender_no := random.randrange(1, 101)) == 1:
                person = PersonGenerator.generate_random_person(gender="other")
            elif 1 < gender_no < 51:
                person = PersonGenerator.generate_random_person(gender="female")
            else:
                person = PersonGenerator.generate_random_person(gender="male")

            PersonGenerator.generate(**person)

        print(f"{generations} persons have been generated.")

    @staticmethod
    def read_in_all_data() -> None:
        PersonGenerator.FEMALE_NAMES = read_in_data_from_text_file(f"{PATH_CLEANED_FILES}{FILE_FEMALE_FIRST_NAMES}")
        PersonGenerator.MALE_NAMES = read_in_data_from_text_file(f"{PATH_CLEANED_FILES}{FILE_MALE_FIRST_NAMES}")
        PersonGenerator.OTHER_NAMES = PersonGenerator.FEMALE_NAMES + PersonGenerator.MALE_NAMES
        PersonGenerator.LAST_NAMES = read_in_data_from_text_file(f"{PATH_CLEANED_FILES}{FILE_LAST_NAMES}")
        PersonGenerator.PHONE_NUMBERS = read_in_data_from_text_file(f"{PATH_CLEANED_FILES}{FILE_PHONE_NUMBERS}")
        PersonGenerator.LOCATIONS = read_in_data_from_json_file(f"{PATH_CLEANED_FILES}{FILE_POST_CODES}")


PATH_CLEANED_FILES = "./data/cleaned/"
FILE_PHONE_NUMBERS = "20k_swedish_phonenumbers.txt"
FILE_FEMALE_FIRST_NAMES = "female_first.txt"
FILE_MALE_FIRST_NAMES = "male_first.txt"
FILE_LAST_NAMES = "lastnames.txt"
FILE_POST_CODES = "postcodes.json"


def main():
    PersonGenerator.generate_data_for_db(100)


if __name__ == "__main__":
    main()
