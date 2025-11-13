#!/usr/bin/env python3
# hello_you.py

import sys

def hello_name(name="you"):
    '''This function returns "Hello and name" passed as terminal argument along with the function
    '''
    print("Hello, {}!".format(name))


if __name__ == "__main__":
    # Checking the number of argument passed along with function from terminal
    arg_count = len(sys.argv) - 1
    # if no argument is passed run the function as default
    if arg_count < 1:
        hello_name()
    else:
        hello_name(sys.argv[1])
