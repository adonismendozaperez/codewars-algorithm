#In this kata, you will do addition and subtraction on a given string. The return value must be a 'string'.
def calculate(str)
    str = str.gsub('plus', '+')
    str = str.gsub('minus','-')
    eval(str).to_s
 end