import json

PATH_RAW_FILES = "./data/raw/"
PATH_CLEANED_FILES = "./data/cleaned/"
FILE_PHONE_NUMBERS = "20k_swedish_phonenumbers.txt"
FILE_FEMALE_FIRST_NAMES = "female_first.txt"
FILE_MALE_FIRST_NAMES = "male_first.txt"
FILE_LAST_NAMES = "lastnames.txt"
FILE_POST_CODES = "postcodes.json"
FILE_HOBBIES = "hobbies.csv"


class DataCleaner:
    @staticmethod
    def clean_first_names_file():
        files = [FILE_FEMALE_FIRST_NAMES, FILE_MALE_FIRST_NAMES]
        for file in files:
            with open(f"{PATH_RAW_FILES}{file}", "r", encoding="utf-8") as file_in:
                contents = [line.replace("\n", "").replace(":", "") for line in file_in.readlines()]

            cleaned_data = []
            for line in contents:
                if len(line) > 1:
                    cleaned_data.append(line)

            with open(f"{PATH_CLEANED_FILES}{file}", "w", encoding="utf-8") as file_out:
                for line in cleaned_data:
                    file_out.write(line + "\n")

    @staticmethod
    def clean_post_codes():
        with open(f"{PATH_RAW_FILES}{FILE_POST_CODES}", "r", encoding="utf-8") as file_in:
            contents = json.load(file_in)

        cleaned_data = []

        for key, value in contents.items():
            location = {
                "street_address": contents[key][0]["Street Name"],
                "street_no": contents[key][0]["Street/Box No."],
                "city": contents[key][0]["City/Locality"],
                "zip_code": contents[key][0]["Postcode"]
            }
            cleaned_data.append(location)

        with open(f"{PATH_CLEANED_FILES}{FILE_POST_CODES}", "w", encoding="utf-8") as file_out:
            json.dump(cleaned_data, file_out)


def clean_phone_numbers():
    with open(PATH_RAW_FILES + FILE_PHONE_NUMBERS, "r", encoding="utf-8") as file_in:
        contents = [line.replace("\n", "") for line in file_in.readlines()]

    cleaned_data = []
    for line in contents:
        cleaned_line = line
        for token in ["[", "]", ",", "\n"]:
            cleaned_line = cleaned_line.replace(token, "")
        cleaned_line = cleaned_line.strip()
        cleaned_data.append(cleaned_line)

    for line in cleaned_data:
        print(line)

    with open(PATH_CLEANED_FILES + FILE_PHONE_NUMBERS, "w", encoding="utf-8") as file_out:
        for line in cleaned_data:
            file_out.write(line + "\n")


def main():
    # DataCleaner.clean_first_names_file()
    # DataCleaner.clean_post_codes()
    pass


if __name__ == "__main__":
    main()
