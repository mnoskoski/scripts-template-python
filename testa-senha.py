import os
import sys
import requests
import string
from itertools import combinations_with_replacement


#file_path=sys.argv[1]

def generatePassword():
    password = string.ascii_lowercase + string.digits
    comb = combinations_with_replacement(password, 10)
    print(list(comb))

if __name__ == "__main__":
    generatePassword()