import random
import string


def get_random(length):
    """
    create random for refresh token in authmk/tokens.py
    :param length: length character for refresh token
    :return: str with Specified Length
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
