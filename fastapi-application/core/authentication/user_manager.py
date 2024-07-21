import logging
from typing import Optional

from fastapi import Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from core.models import User
from core.config import settings
from core.types.user_id import UserIdType


log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):

    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
            self, user: User, request: Optional[Request] = None
    ):
        log.warning("User %s has registered.", user.id)

    async def on_after_forgot_password(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning(
            "User %s has forgot their password. Reset token: %s", user.id, token
        )

    async def on_after_request_verify(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning(
            "Verification requested for user %s. Verification token: %s", user.id, token
        )
