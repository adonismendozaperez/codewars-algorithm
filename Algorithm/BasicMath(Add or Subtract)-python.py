#In this kata, you will do addition and subtraction on a given string. The return value must be a 'string'.
def calculate(parameters):
    for r in (("plus", "+"), ("minus", "-")):
        parameters = parameters.replace(*r)
    return eval(parameters)
    
print(calculate('1plus2plus3plus4'))