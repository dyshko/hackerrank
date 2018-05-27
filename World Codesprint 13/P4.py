#!/bin/python3

import os
import sys

# Complete the fewestOperationsToBalance function below.
def fewestOperationsToBalance(s):
    rs  = []
    for c in s:
        if c == '(':
            rs.append(c)
        if c == ')':
            if len(rs) > 0 and rs[-1] == '(':
                rs.pop()
            else:
                rs.append(c)
    
    a = rs.count(')')
    b = len(rs) - a
    
    if a==b:
        if a==0:
            return 0
        else:
            return 2
    else:
        a, b = max(a,b), min(a,b)
        if b == 0:
            return 1
        else:
            return 2
    
    return 0
                    
    # Return the minimum number of steps to make s balanced.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = fewestOperationsToBalance(s)

    fptr.write(str(result) + '\n')

    fptr.close()