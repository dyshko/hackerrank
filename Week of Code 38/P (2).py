#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minuteToWinIt function below.
def minuteToWinIt(a, k):
    # Return the minimum amount of time in minutes.
    for i in range(len(a)):
        a[i]-=k*i
    
    hist = {}
    for x in a:
        if x not in hist:
            hist[x]=0
        hist[x]+=1
    
    return len(a) - max(hist.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))

    result = minuteToWinIt(a, k)

    fptr.write(str(result) + '\n')

    fptr.close()
