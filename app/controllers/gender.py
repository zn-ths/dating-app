from app.controllers import BaseController
from app.data.models.gender import Gender
from app.data.models.gender import GenderType
from app.data.repository.gender import GenderRepository


class GenderController(BaseController):
    model = Gender
