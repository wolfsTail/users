from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from core.models import Base
from core.models.mixins import IdIntMixin


class User(Base, IdIntMixin, SQLAlchemyBaseUserTable[int]):
    pass