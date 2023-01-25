# Write a python function called find_first_occurrence that
# gets a string haystack and another string needle and returns
# the index of the first occurrence of needle in haystack,
# but False if needle is not present in haystack.

def find_first_occurrence(haystack, needle):
    if haystack.find(needle) == -1:
        return False
    else:
        return haystack.find(needle)

def main():
    # Note: This is only for student-side debugging
    assert find_first_occurrence("hello world", "l") == 2
    assert find_first_occurrence("hello world", "o") == 4
    assert find_first_occurrence("hello world", " ") == 5
    assert find_first_occurrence("hello world", "x") == False

if __name__ == '__main__':
    main()