# from sqlalchemy import Column
# from sqlalchemy import ForeignKey
# from sqlalchemy import Table
#
# from app.data.db import Base

# persons_has_persons = \
#     Table("association", Base.metadata,
#           Column("persons_id", ForeignKey("persons.persons_id")),
#           Column("persons_id", ForeignKey("persons.persons_id")))
#
# persons_prefer_genders = \
#     Table("association", Base.metadata,
#           Column("persons_id", ForeignKey("persons.persons_id")),
#           Column("gender_id", ForeignKey("gender.gender_id")))
#
# persons_has_hobbies = \
#     Table("association", Base.metadata,
#           Column("persons_id", ForeignKey("persons.persons_id")),
#           Column("hobbies_id", ForeignKey("hobbies.hobbies_id")))
