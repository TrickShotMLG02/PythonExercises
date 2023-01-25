# Write a python function called ascii_value that gets as input a string,
# computes the decimal ASCII value of it's first character,
# and returns a string like: The ASCII value of a is 97

def ascii_value(string):
    return f"The ASCII value of {string[0]} is {ord(string[0])}"

def main():
    # Note: This is only for student-side debugging
    assert ascii_value("a") == "The ASCII value of a is 97"
    assert ascii_value("A") == "The ASCII value of A is 65"
    assert ascii_value(" ") == "The ASCII value of   is 32"
    assert ascii_value("Ä") == "The ASCII value of Ä is 196"

    print(ascii_value("a"))
    print(ascii_value("A"))
    print(ascii_value(" "))
    print(ascii_value("Ä"))

# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()