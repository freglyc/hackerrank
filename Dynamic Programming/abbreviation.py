# NOTE: Correct solution but space-time complexity needs to be improved

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    '''
    Input: a -> str, b -> str
    output: 'YES', 'NO'

    DP solution:

    M stores the different str values in a dict that represents a tree
    s.t. the root is at i, left child at 2i+1, right child at 2i+2
    '''
    M = {}
    M[0] = str(a)
    numLower = numL(a) # Finds the number of lower case chars in a
    for i in range(int(math.pow(2, numLower) - 1)): # 2^n-1 splits in the tree
        s_i = firstLower(M[i]) # Finds the first lower case char in M[i]
        M[2*i+1] = toUpper(M[i], s_i) # Case 1: set char to upper case
        M[2*i+2] = remove(M[i], s_i) # Case 2: remoce char from string
    for i in range(int(math.pow(2, numLower)/2), len(M)): # Compares leaves of M with b
        if M[i] == b:
            return 'YES'
    return 'NO'

# finds the first lower case char location in a str a, -1 if none found
def firstLower(a):
    for i in range(len(a)):
        if a[i].islower():
            return i
    return -1

# Counts the number of lower case chars in a str a
def numL(a):
    numLower = 0
    for s_i in range(len(a)):
        if a[s_i].islower():
            numLower += 1
    return numLower

# Given a str a and index i make i upper case
def toUpper(a, i):
    return a[:i] + a[i].upper() + a[i+1:]

# Given a str a and index i remove the value at i
def remove(a, i):
    return a[:i] + a[i+1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
