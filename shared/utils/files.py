import json


def read_in_data_from_text_file(path: str) -> list:
    with open(f"{path}", "r", encoding="utf-8") as file_in:
        contents = [line.replace("\n", "").strip() for line in file_in.readlines()]
    return contents


def read_in_data_from_json_file(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file_in:
        contents = json.load(file_in)
    return contents
