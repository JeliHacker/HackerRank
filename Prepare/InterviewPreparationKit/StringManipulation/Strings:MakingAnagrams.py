# https://www.hackerrank.com/interview/interview-preparation-kit/strings/challenges

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    print(f"len(a) = {len(a)}, len(b) = {len(b)}")
    
    a_dict = {}
    
    answer = 0
    
    for letter in a:
        if not letter in a_dict:
            a_dict[letter] = 1
        else:
            a_dict[letter] += 1
            
    print(a_dict)
            
    for letter in b:
        if letter in a_dict:
            a_dict[letter] -= 1
        else:
            a_dict[letter] = -1
            
    print(a_dict)
            
    for key in a_dict:
        answer += abs(a_dict[key])
        
    return answer
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

