from app.controllers.hobby import HobbyController
from shared.utils.files import read_in_data_from_text_file
from shared.utils.timer import timer


class HobbyGenerator:
    NAME_MAX_LENGTH = 45
    HOBBIES = []

    @staticmethod
    def generate(hobby_name: str) -> None:
        if len(hobby_name) > HobbyGenerator.NAME_MAX_LENGTH:
            raise ValueError(f"Max length of hobby name is {HobbyGenerator.NAME_MAX_LENGTH}.")
        HobbyController.create(hobby_name)

    @staticmethod
    def print_all_hobbies() -> None:
        for hobby in HobbyGenerator.HOBBIES:
            print(hobby)

    @staticmethod
    @timer
    def generate_data_for_db(hobbies: list[str]) -> None:
        for hobby in hobbies:
            try:
                HobbyGenerator.generate(hobby)
            except ValueError:
                print(f"<{hobby}> exceeds the limit of <{HobbyGenerator.NAME_MAX_LENGTH}> and was not added.")


PATH_CLEANED_FILES = "./data/cleaned/"
FILE_HOBBIES = "hobbies.csv"


def main():
    HobbyGenerator.HOBBIES = read_in_data_from_text_file(f"{PATH_CLEANED_FILES}{FILE_HOBBIES}")
    HobbyGenerator.generate_data_for_db(HobbyGenerator.HOBBIES)


if __name__ == "__main__":
    main()
