import unittest

import app.data.db as db
from app.data.models.gender import Gender


class GenderTests(unittest.TestCase):
    def setUp(self) -> None:

        db.Base.metadata.create_all(db.engine)

        # BaseModel.metadata.create_all(self.engine)
        # self.session.add(Gender("female"))
        # self.session.commit()
        gender = Gender(name="female")
        gender.save_to_db()

        gender1 = Gender.find_by_id(1)
        print(gender1)

    def tearDown(self) -> None:
        db.Base.metadata.drop_all(db.engine)

    def test_find_by_id(self):
        gender = Gender.find_by_id(1)
        print(gender)
        self.assertIsNotNone(gender)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
