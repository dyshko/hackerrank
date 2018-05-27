#!/bin/python3

from collections import deque
import os
import sys

INF = None
PATH = {}
DIST = {}

def addPath(p1, p2):
    
    L = list(p1)
    L.append(p2[0])
    R = list(p2)
    mid = -1
    i = 0
    while len(L)>0 and len(R) >i and (L[-1] == R[i]):
        mid = L.pop() 
        i+=1
    
    #print(p1, p2, L + [mid] + R[i:])
    return L + [mid] + R[i:]

def path(nhs, n, a, b):
    
    
    #print("get", a, b)
    
    if (a,b) in PATH:
        return PATH[(a,b)]
    if (b,a) in PATH:
        return PATH[(b,a)]
    
    dist = [INF]*n
    dist[a] = 0
    PATH[(a,a)] = [a]
    queue = deque([(vert, a) for vert in nhs[a].keys()])
   
    
    d = 0
    while dist[b] == INF:
        d+=1
        nsize = len(queue)
        #print(queue, dist)
        for _ in range(nsize):
            #print(queue)
            #print(queue.popleft())
            v, parent = queue.popleft()
            if (v,b) in PATH:
                PATH[(a,b)] = addPath(PATH[(a, parent)],PATH[(v, b)])
                PATH[(b,a)] = PATH[(a,b)]
                return PATH[(a,b)]
                
            if dist[v] == INF:
                dist[v] = d
                PATH[(a,v)] = addPath(PATH[(a, parent)], [v])
                PATH[(v,a)] = PATH[(a, v)]

            for u in nhs[v]:
                if dist[u] == INF:
                    queue.append((u,v))
              
    return PATH[(a,b)]

# Complete the landslide function below.
def landslide(n):
    # Print the answer for each event of type q. Take the road and event data from the standard input.
    slides = {}
    orig = [ {} for i in range(n) ]
    for i in range(n-1):
        a, b = input().split()
        a, b = int(a)-1, int(b)-1
        orig[a][b] = 1
        orig[b][a] = 1
        
    Q = int(input())
    for _ in range(Q):
        l, x, y = input().split()
        x, y = int(x)-1, int(y)-1
        if l=='d':
            slides[(x,y)]=1
            slides[(y,x)]=1
        elif l=='c':
            if (x,y) in slides:
                del slides[(x,y)]
                del slides[(y,x)]
        else:
            p = path(orig, n, x, y)
            #print(x, y, p, slides)
            impos = False
            for i in range(len(p)-1):
                if (p[i],p[i+1]) in slides:
                    impos = True
                    break
                    
            if impos:
                print("Impossible")
            else:
                print(len(p)-1)
    

if __name__ == '__main__':
    n = int(input())

    landslide(n)
