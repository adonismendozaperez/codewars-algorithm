#Alphabet war
# Write a function that accepts fight string consists 
# of only small letters and return who wins the fight. 
# When the left side wins return Left side wins!, when 
# the right side wins return Right side wins!, in other 
# case return Let's fight again!.

def alphabet_war(fight):
    left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_sumatory = 0
    right_sumatory = 0
    
    for f in fight:
        if f in left_side:
            left_sumatory += int(left_side[f])    
        elif f in right_side:
            right_sumatory += int(right_side[f])
    if left_sumatory == right_sumatory:
        return "Let's fight again!"
    else:
        return  "Left side wins!" if left_sumatory > right_sumatory else "Right side wins!" 

print(alphabet_war("zdqmwpbs"))