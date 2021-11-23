from app.controllers.gender import GenderController


class GenderGenerator:
    NAME_MAX_LENGTH = 25
    GENDER_TYPES = ["female", "male", "other"]

    @staticmethod
    def generate(name: str) -> None:
        if len(name) > GenderGenerator.NAME_MAX_LENGTH:
            raise ValueError(f"Max length of gender name is {GenderGenerator.NAME_MAX_LENGTH}.")
        GenderController.create(name)

    @staticmethod
    def generate_data_for_db() -> None:
        for gender_type in GenderGenerator.GENDER_TYPES:
            GenderGenerator.generate(gender_type)


def main():
    GenderGenerator.generate_data_for_db()


if __name__ == "__main__":
    main()
