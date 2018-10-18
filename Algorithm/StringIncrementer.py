# Your job is to write a function which increments a string,
# to create a new string. If the string already ends with a 
# number, the number should be incremented by 1. If the string 
# does not end with a number the number 1 should be appended to 
# the new string.

import re

def increment_string(s):
    number = re.findall(r'\d+', s)
    if number:
        s_number = number[-1]
        s = s.rsplit(s_number, 1)[0]
        number = str(int(s_number) + 1)
        return s + '0' * (len(s_number) - len(number)) + number
    return s + '1'