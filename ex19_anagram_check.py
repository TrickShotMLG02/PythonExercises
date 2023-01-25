def anagram_or_set(string1, string2):
    # return 'anagram', 'set_anagram', or 'no_anagram'

    l1 = sorted(list(string1))
    l2 = sorted(list(string2))

    if l1 == l2:
        return 'anagram'
    elif set(string1) == set(string2):
        return 'set_anagram'
    else:
        return 'no_anagram'