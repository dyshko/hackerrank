#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
A = [int(a_temp) for a_temp in input().strip().split(' ')]
B = [int(b_temp) for b_temp in input().strip().split(' ')]

res = 0
for x in range(1,101):
    acond = True
    for a in A:
        if x%a!=0:
            acond = False
            break
    
    bcond = True
    if acond:
        for b in B:
            if b%x!=0:
                bcond = False
                break
    if acond and bcond:
        res+=1
print(res)
