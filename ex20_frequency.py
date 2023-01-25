from collections import defaultdict

def frequency(string):
    # TODO implement
    # return a dict with the frequency of the letters

    # Example:
    # frequency('Hello World') == {'d': 1, ' ': 1, 'l': 3, 'r': 1, 'H': 1, 'e': 1, 'W': 1, 'o': 2}

    freq = defaultdict(int)

    for letter in string:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    return freq

    pass


def main():
    # Note: This is only for student-side debugging
    assert frequency('Hello World') == {'d': 1, ' ': 1, 'l': 3, 'r': 1, 'H': 1, 'e': 1, 'W': 1, 'o': 2}


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()