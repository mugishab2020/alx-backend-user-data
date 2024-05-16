#!/usr/bin/env python3
'''Using bcrypt module to encrypt the password
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Encrypting the password using bcrypt'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''checking the password validity'''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
