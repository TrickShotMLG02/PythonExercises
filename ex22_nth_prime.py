# Write a function is_x_the_nth_prime(x, n), which determines if the argument x is the n-th prime.
# If x is not a prime number, raise a ValueError stating "Not a prime"
#
# Example:
# is_x_the_nth_prime(2, 1) == True
# is_x_the_nth_prime(97, 25) == True
#
# Hint:
# - Use list comprehension to compute a list of all primes up to x.
# - The any() function returns true of any of the elements in the iterable are Truethy, e.g., any([True, False]) == True
import math


def is_prime(number):
    # 1 is not a prime
    if number == 1:
        return False
    # 2 is a prime
    if number == 2:
        return True
    # all even numbers are not primes
    if number % 2 == 0:
        return False
    # Check if number has divisor between 3 and sqrt(number)
    for i in range(3, math.ceil(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def is_x_the_nth_prime(x, n):
    # TODO implement
    # determines if the argument x is the n-th prime.
    # raise a ValueError stating 'Not a prime' if x is not prime

    if not is_prime(x):
        raise ValueError('Not a prime')

    # get all primes up to x
    primes = [i for i in range(2, x + 1) if is_prime(i)]

    # check if x is the nth prime
    if n > len(primes):
        return False
    elif primes[n - 1] == x:
        return True
    else:
        return False


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