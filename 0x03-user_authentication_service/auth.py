#!/usr/bin/env python3
'''we agonna make the functiion taht encrypts the password
'''

import bcrypt
import os
from user import User
from db import DB
from uuid import UUID
from db import DB


def _hash_password(password: str) -> bytes:
    '''
    generating the hashed password
    '''
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:

        hashed = _hash_password(password)
        try:
            self._db.find_user_by(email=email)
        except Exception:
            return self._db.add_user(email=email, hashed_password=hashed)
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                           user.hashed_password)
        except Exception:
            return False
