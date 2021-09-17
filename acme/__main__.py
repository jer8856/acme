""" __main__ 

This script allows the use of acme module as a command-line tool and
contains the following functions:

    * main - the main function of the script
"""
import sys
from acme import processFile, instructions


def main():
    argv = sys.argv[1:]
    if len(argv) == 1:
        processFile(argv[0])
    else:
        instructions()


if __name__ == '__main__':
    main()
