#!/bin/python3

import sys


T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    x0 = len([x for x in a if x%3==0])%2
    x1 = len([x for x in a if x%3==1])%2
    x2 = len([x for x in a if x%3==2])%2
    if x1==0 and x2 == 0:
        print("Koca")
    else:
        print("Balsa")
    # your code goes here
