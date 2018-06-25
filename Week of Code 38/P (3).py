#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import *

# Complete the leastTimeToInterview function below.
def leastTimeToInterview(n, k, m):
    adj = [ [] for i in range(n) ]
    for _ in range(m):
        v1, v2, t = list(map(int, input().split()))
        v1-=1
        v2-=1
        adj[v1].append([v1,v2,t])
        adj[v2].append([v2,v1,t])
    
    pq = [(0,0)]
    distTo = [1000000000000000]*n
    visited = [False]*n
    distTo[0] = 0
    visited[0] = True
    
    while len(pq) > 0:
        _, v = heappop(pq)
        
        for _, u, t in adj[v]:
            if visited[u]:
                continue
            add = (k - distTo[v]%k) if (distTo[v]//k)%2 == 1 else 0
            if distTo[u] > distTo[v]+t + add:
                distTo[u] = distTo[v]+t + add
                heappush(pq, (distTo[u], u) )
        visited[v] = True
    
    return distTo[n-1]
                
            
        
        
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    m = int(input())

    result = leastTimeToInterview(n, k, m)

    fptr.write(str(result) + '\n')

    fptr.close()
