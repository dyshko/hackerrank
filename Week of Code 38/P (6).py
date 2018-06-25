#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

INF = 1000000000000

def bfs_plus(s, adj, d, a):
    
    D = {}
    D[s] = 0
    arr = [a[s]]
    
    q = deque([s])
    while len(q) > 0:
        v = q.popleft()
        
        for u in adj[v]:
            if u not in D:
                D[u] = D[v] + 1
                if D[u] <= d:
                    arr.append(a[u])
                else:
                    #print(D)
                    return arr
                q.append(u)
    
    return arr

def query(u, d, k, a, adj):
    
    vec = bfs_plus(u, adj, d, a)
    
    if ( len(vec) < k ):
        return -1
    else:
        vec.sort()
        return vec[k-1]
        
# Complete the neighborhoodQueries function below.
def neighborhoodQueries(a):
    # Return the list of answers to all queries. Take the information about edges and queries from standard input.
    
    n = len(a)
    res = []
    
    adj = [ [] for i in range(n) ]
    
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        u, v = u-1, v-1
        adj[u].append(v)
        adj[v].append(u)
    
    Q = int(input())
    for _ in range(Q):
        u, d, k = list(map(int, input().split()))
        u-=1
        res.append( query(u, d, k, a, adj) )
        
    #print(D[4][2])
        
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

   
    
    n = int(input())

    a = list(map(int, input().rstrip().split()))
 
    result = neighborhoodQueries(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
