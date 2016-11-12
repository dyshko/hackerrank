#!/bin/python3

import sys


n = int(input().strip())
a = list(map(int,input().split()))
m = 0
if a[0]!=1:
    m+=1
for i in range(1, n):
    if a[i]!=a[i-1]+1:
        m+=1
print(m)