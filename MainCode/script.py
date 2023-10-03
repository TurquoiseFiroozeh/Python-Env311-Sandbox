"Script.py is only a sandbox for me to test different scenarios"
# import math
import sys
# from os import rename
# from os import rename

import requests

print(f"1:    {sys.version}")
# print(sys.version)
print(f"2:    {sys.executable}")
# print(sys.executable)


def greet(who_to_greet):
    "get a name and return greeting string"
    # greeting = "Hello, {}".format(who_to_greet)
    greeting = f"Hello, {who_to_greet}"
    return greeting


name = input("3:    Your Name?")
print(f"4:    {greet(name)}")
# print(greet("Masoud"))

r = requests.get(url='https://www.google.com', timeout=None)
print(f"5:    Request Code = {r.status_code}")
# print(r.status_code)
