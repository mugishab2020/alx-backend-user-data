#!/usr/bin/env python3
'''
this is the Regex-ing and we are going to make the class 
it will be called filter_datum'''

import re
import logging
import os
from typing import List



def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> List:


