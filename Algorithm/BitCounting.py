#Write a function that takes an integer as input, 
# and returns the number of bits that are equal 
# to one in the binary representation of that number. 
# You can guarantee that input is non-negative.

def countBits(n):
    return bin(n).count("1")
