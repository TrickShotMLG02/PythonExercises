def remaining_debt_and_paid_interest(start_amount, interest_rate, monthly_rate, months):
    # TODO implement
    # for each month, compute the interest that is to be paid. If that interest is higher than the monthly_rate,
    # paying off the loan is impossible. This raise a ValueError stating 'Impossible to pay off'
    # Finally, return a tuple of (remaining_debt, interest_paid), both rounded two decimals.
    # Beware to not compute negative interest after the credit has been paid off
    pass

def main():
    # Note: This is only for student-side debugging
    try:
        remaining_debt_and_paid_interest(100000, 10, 10, 10)
        # your code should raise a ValueError here, hence the assert can never be reached
        assert False
    except ValueError:
        pass
    assert remaining_debt_and_paid_interest(100000, 0.9, 1500, 10) == (85701.81, 701.81)
    assert remaining_debt_and_paid_interest(100000, 0.9, 1500, 100) == (0, 2625.19)


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
