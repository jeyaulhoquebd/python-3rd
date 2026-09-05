# Python program to verify email address using RegEx

import re
patt = "[a-zA=Z0-9]+@[a-zA-Z]+\.(com|net|in)"
def isValid(email):
    if re.search(patt, email):
        print("Email is valid")
    else:
        print("Email is Invalid")