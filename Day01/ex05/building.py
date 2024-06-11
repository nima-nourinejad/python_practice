import sys


def cal(str):
    length = len(str)
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0
    i = 0
    while i < length:
        if str[i] >= 'A' and str[i] <= 'Z':
            upper = upper + 1
        elif str[i] >= 'a' and str[i] <= 'z':
            lower = lower + 1
        elif str[i] >= '0' and str[i] <= '9':
            digit = digit + 1
        elif str[i] == ' ':
            space = space + 1
        elif str[i] in "!\"#$%&'()*+, -./:;<=>?@[]^_`{|}~":
            punctuation = punctuation + 1
        i = i + 1
    print(f"The text contains {length} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """
    This programm takes a single string argument and
    displays the sums of its upper-case,
    characters,
    lower-case
    characters, punctuation characters, digits and spaces.
    """
    try:
        args = sys.argv
        arg_count = len(args) - 1
        if arg_count < 2:
            if arg_count == 0:
                print(f"Enter a single string\n")
                user_input = sys.stdin.readline()
            else:
                user_input = args[1]
            cal(user_input)
        else:
            raise AssertionError("More than one argument is provided")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
