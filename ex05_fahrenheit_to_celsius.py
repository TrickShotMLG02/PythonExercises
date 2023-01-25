def fahrenheit_to_celsius(fahrenheit):
    # TODO implement
    # returns temperature in Celsius, rounded to 2 decimals
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)


def main():
    # Note: This is only for student-side debugging
    assert fahrenheit_to_celsius(64) == 17.78
    assert fahrenheit_to_celsius(100) == 37.78


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
