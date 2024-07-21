from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from core.models import Base
from core.types.user_id import UserIdType

DATABASE_URL = "sqlite+aiosqlite:///./test.db"


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):
    pass


async def get_access_token_db(
    session: AsyncSession = Depends(get_async_session),
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)