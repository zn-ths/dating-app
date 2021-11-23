import unittest

import app.data.db as db
from app.data.models.gender import GenderType
from app.controllers.gender import GenderController
from generator.gender import GenderGenerator


class GenderTests(unittest.TestCase):
    generations = 5

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        db.Base.metadata.create_all(db.engine)

        for _ in range(GenderTests.generations):
            GenderGenerator.generate_data_for_db()

    def tearDown(self) -> None:
        pass

    def tearDownClass(self) -> None:
        db.Base.metadata.drop_all(db.engine)

    def test_create(self):
        gender = GenderController.create(GenderType.FEMALE.value)
        found = GenderController.find_by_id(gender.id)
        self.assertIsNotNone(gender)
        self.assertIsNotNone(found)
        print("Passed test_create()")

    def test_find_by_id(self):
        gender = GenderController.find_by_id(1)
        self.assertIsNotNone(gender)
        print("Passed test_find_by_id()")

    def test_find_by_name(self):
        genders = GenderController.find_all()
        print(f"Len of genders = {len(genders)}")

        other = GenderController.find_by_name(GenderType.OTHER.value)
        self.assertIsNotNone(other)
        print("Passed test_find_by_name()")

    def test_find_all(self):
        genders = GenderController.find_all()
        print(len(genders))
        self.assertTrue(len(genders) >= GenderTests.generations * len(GenderType))
        print("Passed test_find_all()")

    def test_find_all_by_name(self):
        others = GenderController.find_all_by_name(GenderType.OTHER.value)
        self.assertTrue(len(others) >= GenderTests.generations)
        print("Passed test_find_all_by_name()")

    def test_delete(self):
        found_gender = GenderController.find_by_id(5)
        self.assertIsNotNone(found_gender)
        found_gender.delete_from_db()
        deleted_gender = GenderController.find_by_id(5)
        self.assertIsNone(deleted_gender)
        print("Passed test_delete()")

    def test_delete_all(self):
        GenderController.delete_all()
        genders = GenderController.find_all()
        self.assertIsNone(genders)
        print("Passed test_delete_all()")


def main():
    unittest.main()


if __name__ == "__main__":
    main()
