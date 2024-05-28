#!/usr/bin/env python3
'''we agonna make the functiion taht encrypts the password
'''

import bcrypt
import os
from user import User
from db import DB
from uuid import UUID


def _hash_password(password: str) -> bytes:
    '''
    generating the hashed password
    '''
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
