#Small enough? - Beginner
# You will be given an array and a limit value. 
# You must check that all values in the array are 
# below or equal to the limit value. If they are, 
# return true. Else, return false.

def small_enough(array, limit):
    counter = ""
    for arr in array:
        if arr <= limit:
            counter += "True,"
        else:
            counter += "False,"

    if "False" in counter:
        return False
    else:
        return True