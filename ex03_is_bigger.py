def is_bigger(x, y):
    # TODO implement
    # return either '<x> is smaller than <y>', '<x> is bigger than <y>', '<x> is equal to <y>'
    if x > y:
        return '{} is bigger than {}'.format(x, y)
    elif x < y:
        return '{} is smaller than {}'.format(x, y)
    else:
        return '{} is equal to {}'.format(x, y)


def main():
    # Note: This is only for student-side debugging
    assert is_bigger(1, 2) == '1 is smaller than 2'
    assert is_bigger(-1, -2) == '-1 is bigger than -2'
    assert is_bigger(1, 1) == '1 is equal to 1'


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
