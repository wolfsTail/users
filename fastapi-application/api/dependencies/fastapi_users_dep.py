from fastapi_users import FastAPIUsers

from api.dependencies.backend import authentication_backend
from api.dependencies.user_manager import get_user_manager
from core.models import User
from core.types.user_id import UserIdType


fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
