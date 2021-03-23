#!/usr/bin/python

import subprocess
import sys

command = subprocess.Popen(['date'])
print("Hello World", command)