# NOTE: Correct Solution

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    '''
    Input: arr -> list
    Output: -> int

    Recurrence: OPT(j) = max(a_j + OPT(j-2), OPT(j-1))
    '''
    M = {}
    M[-1] = 0
    M[0] = 0
    for i in range(1, len(arr) + 1):
        M[i] = max(arr[i-1] + M[i-2], M[i-1])
    return M[len(arr)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
