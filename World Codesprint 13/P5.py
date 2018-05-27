#!/bin/python3

import os
import sys

def foo_res(hist, c):
    n = len(hist)
    
    #print(hist, c)
    if n <= 1+c:
        return 0
    
    if c==0:
        t_sum = sum(hist[1:])
        return (t_sum*(t_sum-1))//2
    
    res = 0
    r_sum = sum(hist[1:1+c])
    for i in range(1, n - c):
        #print("inloop",i, r_sum, n, c)
        res += hist[i]*r_sum - (hist[i]*(hist[i]+1))//2
        r_sum += hist[i+c] - hist[i]
    res += hist[n-c]*r_sum - (hist[n-c]*(hist[n-c]+1))//2
    
    t_sum = sum(hist[1:])
    res = (t_sum*(t_sum-1))//2 - res
    return res

#y to reduce
#x to grow
def foo_update(hist, x, y):
    #x -> x+1
    #y -> y-1
    hist[x]-=1
    hist[y]-=1
    while x+y >= len(hist):
        hist.append(0)
    hist[x+y]+=1
    

# Complete the competitiveTeams function below.
def competitiveTeams(n, q):
    # Print the answer for each query of type 2. Take the query data from the standard input.
    group = [None]*(n+1)
    for i in range(n):
        group[i+1] = [i+1]
    
    hist_groups = [0]*2
    hist_groups[1] = n
    
    for _ in range(q):
        input_array = input().split()
        #print("querry",input_array)
        if len(input_array) == 3:
            x, y = int(input_array[1]), int(input_array[2])
            x, y = int(x), int(y)
            gx = group[x]
            gy = group[y]
            if id(gx) == id(gy):
                continue
            ###update len_groups
            foo_update(hist_groups, len(gx), len(gy))
            ###update groups
            group[x] += group[y]
            for p in group[y]:
                group[p] = group[x]
            
            
        else:
            c = int(input_array[1])
            print(foo_res(hist_groups, c))
    

if __name__ == '__main__':
    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    competitiveTeams(n, q)
