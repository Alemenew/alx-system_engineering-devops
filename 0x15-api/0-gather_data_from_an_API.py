#!/usr/bin/python3

"""
Using https://jsonplaceholder.typicode.com
retruns info about emplyee TODO progress
Implemented using recursion

"""

import re
import requests
import sys


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__mian__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sus.argv[1])
            user_res = requests.get ('{}/users/{}'.)
