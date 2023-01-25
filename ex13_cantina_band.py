# Write a python function called repeat_string that gets as input a string
# and a maximum length. The function should print out the string until
# the maximum length of the output is reached.
#
# Example:
# repeat_string("abc", 10) should print out:
# abcabcabca
#
# repeat_string("abc", 5) should print out:
# abcab
#
# repeat_string("abc", 3) should print out:
# abc
#
# repeat_string("abc", 2) should print out:
# ab
#
# repeat_string("abc", 1) should print out:
# a
#

def repeat_string(string, max_length):
    tmp = ""
    while len(tmp) + len(string) < max_length:
        tmp += string

    if max_length - len(tmp) > 0:
        tmp += string[:max_length - len(tmp)]
    else:
        tmp = ""

    return tmp

def main():
    # Note: This is only for student-side debugging
    assert repeat_string("abc", 10) == "abcabcabca"
    assert repeat_string("abc", 5) == "abcab"
    assert repeat_string("abc", 3) == "abc"
    assert repeat_string("abc", 2) == "ab"
    assert repeat_string("abc", 1) == "a"

if __name__ == '__main__':
    main()