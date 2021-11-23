from app.controllers.gender import GenderController
from app.data.models.gender import Gender
from app.data.models.gender import GenderType
from app.data.repository.gender import GenderRepository

GENERATIONS = 5


def test_set_up():
    print("-" * 40)
    print(f"Setting up test data...")
    print("-" * 40)

    gender_types = ["female", "male", "other"]
    for _ in range(GENERATIONS):
        for gt in gender_types:
            GenderController.create(gt)


def test_find_by_id():
    print("\n" + ("-" * 40))
    print(f"Testing {GenderController.find_by_id.__name__}")
    print("-" * 40)

    genders = GenderController.find_all()
    if genders:
        found = GenderController.find_by_id(genders[0].id)
        if found:
            print(f"\nGender with id={found.id}:\n{found}")


def test_find_by_name():
    print("\n" + ("-" * 40))
    print(f"Testing {GenderController.find_by_name.__name__}")
    print("-" * 40)

    name = "other"
    if found := GenderController.find_by_name(name):
        print(f"\nGender with name={name}:\n{found}")


def test_find_all():
    print("\n" + ("-" * 40))
    print(f"Testing {GenderController.find_all.__name__}")
    print("-" * 40)

    genders = GenderController.find_all()
    expected = GENERATIONS * len(GenderType)
    assert len(genders) >= expected
    print(f"\nFound {expected} rows.")


def test_find_all_by_name():
    print("\n" + ("-" * 40))
    print(f"Testing {GenderController.find_all_by_name.__name__}")
    print("-" * 40)

    females = GenderController.find_all_by_name("female")
    assert len(females) >= GENERATIONS
    print(f"\nFound {len(females)} rows.")


def test_delete_by_id():
    print("\n" + ("-" * 40))
    print(f"Testing {GenderController.delete_by_id.__name__}")
    print("-" * 40)

    genders = GenderController.find_all()

    if genders:
        gender_id = genders[0].id
        GenderController.delete_by_id(gender_id)
        print(f"\nGender with id={gender_id} deleted.")


def test_delete_all():
    print("\n" + ("-" * 40))
    print(f"Testing {GenderController.delete_all.__name__}")
    print("-" * 40)

    GenderController.delete_all()

    genders = GenderController.find_all()
    assert not genders
    print(f"\nNo rows found. Delete all was successful.")


def main():
    test_set_up()
    test_find_by_id()
    test_find_by_name()
    test_find_all()
    test_find_all_by_name()
    test_delete_by_id()
    test_delete_all()


if __name__ == "__main__":
    main()
