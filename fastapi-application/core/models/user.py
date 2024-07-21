from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Base
from core.models.mixins import IdIntMixin
from core.types.user_id import UserIdType


class User(Base, IdIntMixin, SQLAlchemyBaseUserTable[UserIdType]):
    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)