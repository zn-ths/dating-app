from app.controllers import BaseController
from app.controllers.person import PersonController
from app.data.models.person import Person
from app.data.repository.person import PersonRepository

GENERATIONS = 100


# def test_set_up():
#     from generator.person import PersonGenerator
#
#     print("-" * 40)
#     print(f"Setting up test data...")
#     print("-" * 40)
#
#     PersonGenerator.generate_data_for_db(GENERATIONS)


def test_find_by_id():
    print("\n" + ("-" * 40))
    print(f"Testing {PersonController.find_by_id.__name__}")
    print("-" * 40)

    hobbies = PersonController.find_all()
    if hobbies:
        found = PersonController.find_by_id(hobbies[0].id)
        if found:
            print(f"\nPerson with id={found.id}:\n{found}")


def test_find_by_name():
    print("\n" + ("-" * 40))
    print(f"Testing {PersonController.find_by_name.__name__}")
    print("-" * 40)

    people = PersonController.find_all()
    if people:
        name = people[0].name
        if found := PersonController.find_by_name(name):
            print(f"\nPerson with name={name}:\n{found}")


def test_find_all():
    print("\n" + ("-" * 40))
    print(f"Testing {PersonController.find_all.__name__}")
    print("-" * 40)

    people = PersonController.find_all()
    result = len(people)
    expected = GENERATIONS
    assert result >= expected
    print(f"\nFound {result} rows.")


# def test_find_all_by_name():
#     print("\n" + ("-" * 40))
#     print(f"Testing {PersonController.find_all_by_name.__name__}")
#     print("-" * 40)
#
#     people = PersonController.find_all_by_name("John")
#     expected = 1
#     result = len(people)
#     assert result >= expected
#     print(f"\nFound {result} rows.")


def test_delete_by_id():
    print("\n" + ("-" * 40))
    print(f"Testing {PersonController.delete_by_id.__name__}")
    print("-" * 40)

    people = PersonController.find_all()

    if people:
        person_id = people[0].id
        PersonController.delete_by_id(person_id)
        print(f"\nPerson with id={person_id} deleted.")


def test_delete_all():
    print("\n" + ("-" * 40))
    print(f"Testing {PersonController.delete_all.__name__}")
    print("-" * 40)

    PersonController.delete_all()

    person = PersonController.find_all()
    assert not person
    print(f"\nNo rows found. Delete all was successful.")


def main():
    # test_set_up()
    test_find_by_id()
    test_find_by_name()
    test_find_all()
    # test_find_all_by_name()
    test_delete_by_id()
    test_delete_all()

    # TODO: FIND ALL
    # hobbies = Hobby.find_all()

    # TODO: FIND BY FIRST_NAME
    # TODO: FIND BY LAST_NAME
    # TODO: FIND BY FULL_NAME

    # TODO: __repr__(), __str__(), to_dict()

    # TODO: CREATE
    # TODO: DELETE

    # TODO: UPDATE

    # TODO: FIND BY PATTERN

    pass
