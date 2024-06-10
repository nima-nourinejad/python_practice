import sys

args = sys.argv
argc = len(args) - 1

if argc > 1:
    print("AssertionError: More than one argument is provided")
elif argc == 1:
    try:
        integer = int(args[1])
        remainder = integer % 2
        if remainder == 1:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except ValueError:
        print("AssertionError: Argument is not an integer")
