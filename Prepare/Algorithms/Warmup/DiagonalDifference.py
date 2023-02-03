# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diagonal = 0
    right_diagonal = 0
    right = len(arr) - 1
    
    for i in range(len(arr)):
        print(arr[i][i])
        left_diagonal += arr[i][i]
        right_diagonal += arr[i][right]
        
        right -= 1
        
    answer = abs(right_diagonal - left_diagonal)
      
    print(right_diagonal, left_diagonal)
    print(answer)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

