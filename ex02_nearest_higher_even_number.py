def nearest_higher_even_number(x):
    # TODO: implement
    # returns an int
    if x % 2 == 0:
        return x + 2
    else:
        return x + 1


def main():
    # Note: This is only for student-side debugging
    assert (nearest_higher_even_number(5) == 6)
    assert (nearest_higher_even_number(4) == 6)
    assert (nearest_higher_even_number(0) == 2)
    assert (nearest_higher_even_number(-1) == 0)


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()