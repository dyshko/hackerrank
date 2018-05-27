#!/bin/python3

import os
import sys

# Complete the howManyGoodSubarrays function below.
def howManyGoodSubarrays(A, m, k):
    N = len(A)
    if N == 0:
        return 0
    if N == 1:
        return 1 if (A[0]%m == k) else 0
    
    n = N//2
    #print(A[:n], A[n:])
    res = howManyGoodSubarrays(A[:n], m, k) + \
          howManyGoodSubarrays(A[n:], m, k)
    
    left_hist = {}
    p = 1
    for i in range(n-1, -1, -1):
        p = (p*A[i])%m
        if p not in left_hist:
            left_hist[p] = 0
        left_hist[p] += 1
        
    #print(left_hist)
    p = 1
    for i in range(n, N):
        p = (p*A[i])%m
        #xp = kp^-1 (mod m)
        if p == 0:
            if k==0:
                res+=n
        else:
            xp = (k*pow(p, m-2, m))%m
            if xp in left_hist:
                res+=left_hist[xp]
                
            
    #print(A, res)
            
    return res
    
    # Return the number of good subarrays of A.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nmk = input().split()

        n = int(nmk[0])

        m = int(nmk[1])

        k = int(nmk[2])

        A = list(map(int, input().rstrip().split()))

        result = howManyGoodSubarrays(A, m, k)

        fptr.write(str(result) + '\n')

    fptr.close()