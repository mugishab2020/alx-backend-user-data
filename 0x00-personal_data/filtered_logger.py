#!/usr/bin/env python3
'''
this is the Regex-ing and we are going to make the class
it will be called filter_datum'''

import re
import logging
import os
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> List:
    '''Function to return the log message obfuscated'''
    return re.sub(fr'({"|".join(fields)})=[^{separator}]+',
                  f'\\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''NotImplementedError'''
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)
