# Write a function called decode that gets as input an encoded string (either as bytestring or string) as well as an optional parameter encoding defaulting to base64. Your function should decode this string with the given algorithm and return it as string.
# The function should support base16, base32, base64, and base85. In case of an Exception or missing support your function should return an empty string.
#
# Hint: import base64
#
# You must use the base64 library!

import base64

def decode(string, encoding='base64'):

    if encoding == 'base16':
        try:
            return base64.b16decode(string).decode('utf-8')
        except:
            return ''
    elif encoding == 'base32':
        try:
            return base64.b32decode(string).decode('utf-8')
        except:
            return ''
    elif encoding == 'base64':
        try:
            return base64.b64decode(string).decode('utf-8')
        except:
            return ''
    elif encoding == 'base85':
        try:
            return base64.b85decode(string).decode('utf-8')
        except:
            return ''
    else:
        return ''
    pass
