def capitalize_first(string):
    # TODO implement
    # return an str with the first letter capitalized
    # and the rest of the string unchanged
    return string[0].upper() + string[1:]
    pass


def main():
    # Note: This is only for student-side debugging
    assert capitalize_first('helloWorld') == 'HelloWorld'
    assert capitalize_first('A') == 'A'


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
