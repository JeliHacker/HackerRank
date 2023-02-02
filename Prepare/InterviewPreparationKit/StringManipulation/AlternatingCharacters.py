# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    new_string = list(s)
    print(s, new_string)
    left = 0
    right = 1
    answer = 0
    
    if len(s) == 1:
        return 0
    
    while left < right and right < len(s):
        left_letter = new_string[left]
        right_letter = new_string[right]
        
        if left_letter == right_letter:
            new_string[right] = '_'
            right += 1
        else:
            left = right
            right += 1
            
    for letter in new_string:
        if letter == '_':
            answer += 1
            
    return answer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

