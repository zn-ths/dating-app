from datetime import date

from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.data.models import BaseModel
from app.data.models.gender import Gender


class Person(BaseModel):
    __tablename__ = "persons"
    __table_args__ = {"schema": "dating-db"}

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(length=45), nullable=False)
    surname = Column(String(length=45), nullable=False)
    birthday = Column(Date, nullable=False)
    have_children = Column(Boolean)
    street_address = Column(String(length=120), nullable=False)
    zip_code = Column(String(length=15), nullable=False)
    city = Column(String(length=150), nullable=False)
    country = Column(String(length=45), nullable=False)
    phone_number = Column(String(length=45), nullable=False)
    email = Column(String(length=45), nullable=False)

    gender_id = Column(Integer, ForeignKey("gender.id"))
    gender = relationship(Gender)

    def __init__(self,
                 name: str,
                 surname: str,
                 birthday: date,
                 have_children: bool,
                 street_address: str,
                 zip_code: str,
                 city: str,
                 country: str,
                 phone_number: str,
                 email: str,
                 gender_id: int) -> None:
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.have_children = have_children
        self.street_address = street_address
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.phone_number = phone_number
        self.email = email
        self.gender_id = gender_id
