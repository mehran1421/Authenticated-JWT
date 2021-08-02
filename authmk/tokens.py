import jwt
from django.conf import settings
from datetime import datetime, timedelta
from extention.utils import get_random


def get_access_token(payload):
    """
    get access token for user with HS256 algorithm
    access token expire each 5 minutes
    :param payload:
    :return:
    """
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5), **payload},
        settings.SECRET_KEY,
        algorithm="HS256"
    )


def get_refresh_token(payload):
    """
    get refresh token for user
    refresh token expire after 365 day
    with refresh token can without request to database find user
    :param payload:
    :return:
    """
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data": get_random(10)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )
