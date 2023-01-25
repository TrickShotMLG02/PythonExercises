def divisible_without_rest(x, y):
    # TODO: implement
    # returns True or False

    return x % y == 0


def main():
    # Note: This is only for student-side debugging
    assert (divisible_without_rest(5, 2) is False)
    assert (divisible_without_rest(4, 2) is True)
    assert (divisible_without_rest(2, 8) is False)
    assert (divisible_without_rest(2, 2) is True)


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
