#Convert string to camel case

# Complete the method/function so that it converts 
# dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized 
# only if the original word was capitalized.

def to_camel_case(text):
    result = ""
    count = 0
    for val in text.replace("-","_").split("_"):
        count += 1
        if count != 1:
            result += "".join(val.capitalize())
        else:
            result += "".join(val)
    return result