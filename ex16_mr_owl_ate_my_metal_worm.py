# Write a python function called palindrome that checks if it's
# input string is a palindrome ignoring all spaces and capitalisation.

def palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def main():
    # Note: This is only for student-side debugging
    assert palindrome("abba") == True
    assert palindrome("aBbA") == True
    assert palindrome("aBbA ") == True
    assert palindrome("aBbA S ") == False

if __name__ == '__main__':
    main()
