def is_x_the_nth_prime(x, n):
    # TODO implement
    # determines if the argument x is the n-th prime.
    # raise a ValueError stating 'Not a prime' if x is not prime
    pass


def main():
    # Note: This is only for student-side debugging
    assert is_x_the_nth_prime(2, 1) is True
    assert is_x_the_nth_prime(97, 25) is True
    try:
        is_x_the_nth_prime(4, 2)
        # this should have thrown an error and the assert should not be triggered
        assert False
    except ValueError as e:
        assert (str(e) == 'Not a prime')


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
