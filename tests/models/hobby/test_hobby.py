from app.controllers import BaseController
from app.controllers.hobby import HobbyController
from app.data.models.hobby import Hobby
from app.data.repository.hobby import HobbyRepository

GENERATIONS = 5
HOBBIES = ["Bowling", "Chess", "Sudoku", "Movies", "Sports", "Food"]


def test_set_up():
    print("-" * 40)
    print(f"Setting up test data...")
    print("-" * 40)

    for hobby in HOBBIES:
        HobbyController.create(hobby)


def test_find_by_id():
    print("\n" + ("-" * 40))
    print(f"Testing {HobbyController.find_by_id.__name__}")
    print("-" * 40)

    hobbies = HobbyController.find_all()
    if hobbies:
        found = HobbyController.find_by_id(hobbies[0].id)
        if found:
            print(f"\nHobby with id={found.id}:\n{found}")


def test_find_by_name():
    print("\n" + ("-" * 40))
    print(f"Testing {HobbyController.find_by_name.__name__}")
    print("-" * 40)

    name = "Food"
    if found := HobbyController.find_by_name(name):
        print(f"\nHobby with name={name}:\n{found}")


def test_find_all():
    print("\n" + ("-" * 40))
    print(f"Testing {HobbyController.find_all.__name__}")
    print("-" * 40)

    genders = HobbyController.find_all()
    result = len(genders)
    expected = len(HOBBIES)
    assert result >= expected
    print(f"\nFound {result} rows.")


def test_find_all_by_name():
    print("\n" + ("-" * 40))
    print(f"Testing {HobbyController.find_all_by_name.__name__}")
    print("-" * 40)

    movies = HobbyController.find_all_by_name("Movies")
    expected = 1
    result = len(movies)
    assert result >= expected
    print(f"\nFound {result} rows.")


def test_delete_by_id():
    print("\n" + ("-" * 40))
    print(f"Testing {HobbyController.delete_by_id.__name__}")
    print("-" * 40)

    hobbies = HobbyController.find_all()

    if hobbies:
        hobby_id = hobbies[0].id
        HobbyController.delete_by_id(hobby_id)
        print(f"\nHobby with id={hobby_id} deleted.")


def test_delete_all():
    print("\n" + ("-" * 40))
    print(f"Testing {HobbyController.delete_all.__name__}")
    print("-" * 40)

    HobbyController.delete_all()

    hobbies = HobbyController.find_all()
    assert not hobbies
    print(f"\nNo rows found. Delete all was successful.")


def main():
    test_set_up()
    test_find_by_id()
    test_find_by_name()
    test_find_all()
    test_find_all_by_name()
    test_delete_by_id()
    test_delete_all()

    # WORKS
    # hobbies = Hobby.find_all()

    # WORKS
    # for hobby in hobbies:
    # print(hobby.__repr__())
    # print(hobby.__str__())
    # print(hobby.to_dict())

    # TODO: CREATE
    # TODO: DELETE

    # TODO: UPDATE

    # TODO: FIND BY PATTERN


if __name__ == "__main__":
    main()
