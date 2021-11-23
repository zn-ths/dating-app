import unittest

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from app.data.db import Base
# # from app.data.models import BaseModel
from app.data.models.gender import Gender
from generator.gender import GenderGenerator


Base = declarative_base()


class GenderTests(unittest.TestCase):
    generations = 5

    def setUp(self) -> None:
        self.engine = create_engine("sqlite:///:memory")
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()
        Base.metadata.create_all(self.engine)

        self.gender = Gender("other")
        self.session.add(self.gender)
        self.session.commit()

    # @classmethod
    # def setUpClass(cls) -> None:
    #
    #     BaseModel.metadata.create_all(db.engine)
    #
    #     for _ in range(GenderTests.generations):
    #         GenderGenerator.generate_data_for_db()

    def tearDown(self) -> None:
        Base.metadata.drop_all(self.engine)

    # def tearDownClass(self) -> None:
    #     BaseModel.metadata.drop_all(db.engine)

    # def test_create(self):
    #     gender = GenderController.create(GenderType.FEMALE.value)
    #     found = GenderController.find_by_id(gender.id)
    #     self.assertIsNotNone(gender)
    #     self.assertIsNotNone(found)
    #     print("Passed test_create()")

    def test_find_by_id(self):
        expected = self.gender
        result = self.session.query(Gender).filter_by(id=1).first()
        print(result)
        self.assertEqual(result, expected)
        print("Passed test_find_by_id()")


def main():
    unittest.main()


if __name__ == "__main__":
    main()
