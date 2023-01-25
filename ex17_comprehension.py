# Write a python function called list_of_squares that returns a list of all squares from 1 up to (including) its input n.
#
# Example: list_of_squares(3) == [1, 4, 9]
#
# You must use list comprehension for this task

def list_of_squares(n):
    return [x**2 for x in range(1, n+1)]


def main():
    assert list_of_squares(3) == [1, 4, 9]
    assert list_of_squares(5) == [1, 4, 9, 16, 25]
    assert list_of_squares(10) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

if __name__ == '__main__':
    main()