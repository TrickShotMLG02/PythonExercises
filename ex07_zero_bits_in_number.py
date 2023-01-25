def zero_bits_in_number(hexadecimal):
    # TODO implement
    # takes str, return int
    return (bin(int(hexadecimal, 16)))[2:].count('0')


def main():
    # Note: This is only for student-side debugging
    assert (zero_bits_in_number('a') == 2)


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
