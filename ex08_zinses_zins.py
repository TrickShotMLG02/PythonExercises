def zinses_zins(base_amount, rate_in_percent, years):
    # TODO implement
    # return int or float, rounded to two decimals
    return round(base_amount * (1 + rate_in_percent / 100) ** years, 2)


def main():
    # Note: This is only for student-side debugging
    assert zinses_zins(1000, 5, 2) == 1102.5


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
