from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Base
from core.models.mixins import IdIntMixin


class User(Base, IdIntMixin, SQLAlchemyBaseUserTable[int]):
    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, User)