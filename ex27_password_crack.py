# Write a function pwd_crack that gets four inputs: The known start of a user's password as string, a sha1 hash of the full password as hex string,
# length of the full password, and optionally a charset (default: string.ascii_lowercase). The function should brute force the parts of the password
# are missing and return the missing characters.
#
# Hint: You might want to take a look at the itertools library.
#
# You must use the itertools library and the sha1 function from the hashlib library.

import hashlib, itertools, string

def pwd_crack(start, hash_hex, length, charset=string.ascii_lowercase):
    # return the missing characters of the password

    n = length - len(start)
    print(n)
    list = itertools.product(charset, repeat=n)

    for entry in list:
        if hashlib.sha1((start + ''.join(entry)).encode()).hexdigest() == hash_hex:
            return ''.join(entry)