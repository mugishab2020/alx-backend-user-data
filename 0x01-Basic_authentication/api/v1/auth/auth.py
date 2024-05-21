#!/usr/bin/env python3


from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True
        if excluded_paths is None or excluded_paths.isEmpty():
            return True
        if path in excluded_paths:
            return False
        if not path.endswith('/'):
            path += '/'
        normalized_excluded_paths = [
            p if p.endswith('/') 
            else p + '/' for p in excluded_paths
        ]

        if path in normalized_excluded_paths:
            return False
        return True        

    ''' def authorization_header(self, request=None) -> str:
        return None'''
    def authorization_header(self, request=None) -> str:
        '''Request validation'''
        if not request:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')


    def current_user(self, request=None) -> TypeVar('User'):
        return None
