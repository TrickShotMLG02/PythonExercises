# Write a function requests_post_json(nonce). This should first make a GET request to https://python.cysec1.de/challenges/json_post. This provides you with a CAPTCHA. Solve the CAPTCHA and post the result as the parameter solution alongside the nonce. Your POST request must use JSON. If done correctly, the answer is a JSON, which contains a key called hmac. This should be returned.
# Example:
#
# <-- {'captcha': 'JqckbkJtDK ', 'description': 'please run the requested function on this captcha', 'requested_function': 'lower'}
# --> {'solution': 'jqckbkjtdk ', 'nonce': 'some_nonce'}
# <-- {'hmac': '8e28707558b96796c6ceb6d8b64616846a324e42'}
#
# Hints:
# the server identifies you through a Session
# getattr(str, 'lower') == str.lower
# 'some_string'.lower() == str.lower('some_string')