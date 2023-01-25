# Write a python function called lower_case_and_remove_vowels that
# converts its input string to lowercase and removes all vowels from it.

def lower_case_and_remove_vowels(string):
    return string.lower().replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")

def main():
    # Note: This is only for student-side debugging
    assert lower_case_and_remove_vowels("Hello World") == "hll wrld"
    assert lower_case_and_remove_vowels("ÄÖÜ") == "äöü"
    assert lower_case_and_remove_vowels("aeiou") == ""
    assert lower_case_and_remove_vowels("a") == ""
    assert lower_case_and_remove_vowels("A") == ""
    assert lower_case_and_remove_vowels(" ") == " "

if __name__ == '__main__':
    main()
