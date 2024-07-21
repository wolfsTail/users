from fastapi_users.authentication import BearerTransport


bearer_transport = BearerTransport(
    # update url
    tokenUrl="auth/jwt/login"
)