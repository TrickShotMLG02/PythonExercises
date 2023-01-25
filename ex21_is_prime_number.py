# Write a function is_prime which takes a number and checks if it's a prime. This function must use a for loop to check.
#
# Hints:
# - math.ceil
# - math.sqrt

import math
def is_prime(number):
    # return True if number is prime, False otherwise

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

def main():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(9) is False

if __name__ == '__main__':
    main()
