#!/usr/bin/python3

import subprocess
from shlex import quote
import sys

filename = sys.argv[1]

def perfomShell(*args):
	command = 'ls -a {}'.format(quote(filename))
	#print(command)
	subprocess.call(command, shell=True)


if __name__ == '__main__':
	perfomShell()
