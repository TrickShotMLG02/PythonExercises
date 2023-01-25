# Write a python function called n_nn_nnn that as input takes a positive integer n and computes nnn+nn+n (e.g., n_nn_nnn(5): 555+55+5.

def n_nn_nnn(n):
    # TODO implement
    return int(str(n) * 3) + int(str(n) * 2) + int(str(n) * 1)


def main():
    # Note: This is only for student-side debugging
    assert n_nn_nnn(1) == 123
    assert n_nn_nnn(10) == 102030


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
