#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import *

class Edge:
    def __init__(self, u, v, br):
        self.u = min(u,v)
        self.v = max(u,v)
        self.br = br
        
    def other(self, v):
        return self.u if v == self.v else self.v
        
    def str(self):
        return "("+str(self.u)+"- " + str(self.br) + " -"+str(self.v)+")"

INF = 1000000000000000

def dijkstra(n, adj):
    pq = [(0,0)]
    distTo = [INF]*n
    edgeTo = [None]*n
    visited = [False]*n
    distTo[0] = 0
    visited[0] = True
    
    while len(pq) > 0:
        _, v = heappop(pq)
        
        for edg in adj[v]:
            u = edg.other(v)
            if visited[u]:
                continue
            if distTo[u] > distTo[v] + edg.br:
                distTo[u] = distTo[v] + edg.br
                edgeTo[u] = edg
                heappush(pq, (distTo[u], u) )
        visited[v] = True
    
    path = []
    u = n-1
    while edgeTo[u] is not None:
        path.append(edgeTo[u])
        u = edgeTo[u].other(u)
    return path

def newmax(a, t):
    n = len(a)
    a.append(0)
    i = 0
    res = a[0]
    S = 0
    while (t > 0 and i < n):
        S+=a[i]
        if a[i] == a[i+1]:
            i+=1
            continue
        
        Vmax = S - a[i+1]*(i+1)
        Vmin = S - a[i]*(i+1)
        
        if (t >= Vmax):
            res = a[i+1]
        elif (t >= Vmin):
            res = a[i] - (t - Vmin) // (i+1)
            break
        else:
            break

        i+=1
    return res
    
# Complete the minimumBrokenness function below.
def minimumBrokenness(n, m, k, t):
    
    adj = [ [] for i in range(n) ]
    edges = []
    
    for _ in range(m):
        v1, v2 = list(map(int, input().split()))
        e = Edge(v1, v2, 0)
        adj[v1].append(e)
        adj[v2].append(e)
        edges.append(e)
        
    for _ik in range(k):
        path = dijkstra(n, adj)
        for edge in path:
            edge.br+=1
            
        #print(" ".join( [edge.str() for edge in path] ))
        #print(" ".join( [edge.str() for edge in edges] ))
            
    s = [ max(edge.br - 1, 0) for edge in edges ]
    s.sort(reverse = True)
    #print(s)
    
    return newmax(s, t)
    # Return the minimum possible brokenness of a truck among all k trucks driving from city 0 to city n-1. Take the information about roads from standard input.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmkt = input().split()

    n = int(nmkt[0])

    m = int(nmkt[1])

    k = int(nmkt[2])

    t = int(nmkt[3])

    result = minimumBrokenness(n, m, k, t)

    fptr.write(str(result) + '\n')

    fptr.close()
