#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from functools import total_ordering

class snode:
    def __init__(self, w, time):
        self.w = w
        self.time = time
        
    def str(self):
        return "("+str(self.w)+","+str(self.time)+")"
    
class link:
    def __init__(self):
        self.link = []
        self.sum = 0
        self.max_time = -1
        
    def add(self, snode):
        self.link.append(snode)
        self.sum += snode.w
        self.max_time = snode.time
    
    def remove(self):
        snode = self.link.pop()
        self.sum -= snode.w
        if not self.empty():
            self.max_time = self.link[-1].time
        
    def empty(self):
        return len(self.link) == 0
    
    def print(self, pref):
        print(pref+"link:", "sum",  self.sum, "maxtime", self.max_time, " ".join( [snode.str() for snode in self.link  ]))
    
    def __lt__(self, other):
        return not (self.sum < other.sum)
    
    def __eq__(self, other):
        return self.max_time == other.max_time

class Node:
    
    def __init__(self):
        self.links = []
        self.max = 0
        self.max_time = -1
        
    def addNew(self, w, time):
        l = link()
        l.add(snode(w, time))
        heapq.heappush(self.links, l)
        if w > self.max:
            self.max = w
            self.max_time = time
    
    def update(self):
        if len(self.links) == 0:
            self.max = 0
            self.max_time = -1
        else:
            maxlink = self.links[0]
            self.max = maxlink.sum
            self.max_time = maxlink.max_time
    
    def removeMax(self):
        link = heapq.heappop(self.links)
        if self.links is None:
            self.max = 0
            self.max_time = -1
        else:
            link.remove()
            if not link.empty():
                heapq.heappush(self.links, link)
            self.update()
            
    def addToMax(self, w, time):
        if len(self.links) == 0:
            self.addNew(w, time)
        else:
            link = heapq.heappop(self.links)
            link.add(snode(w, time))
            heapq.heappush(self.links, link)
            self.update()
    
    def print(self, pref):
        print(pref+"max", self.max, "maxtime", self.max_time, "links:")
        for link in self.links:
            link.print(pref+"  ")
    
class Cycle:
    def __init__(self, w):
        self.w = w
        self.total = sum(w)
        self.n = len(w)
        self.nodes = [ Node() for i in range(len(w)) ]
        
    def findFar(self, Id):
        bestNode = None
        bestDist = 0
        bestTime = -1
        
        i = Id-1
        if (i == -1):
                i = n-1
        
        distToCurrent = self.total - w[i]
        while True:
            
            val = self.nodes[i].max + distToCurrent
            if (val > bestDist) or (val == bestDist and bestTime < self.nodes[i].max_time):
                bestNode = self.nodes[i]
                bestDist = val
                bestTime = self.nodes[i].max_time
            
            if (i == Id):
                break
            
            i-=1
            if (i == -1):
                i = n-1
        
            distToCurrent -= w[i]
            
        
        return bestDist, bestNode
    
    def print(self):
        print("")
        for i in range(self.n):
            print("Node:", i)
            self.nodes[i].print("  ")

# Complete the cyclicalQueries function below.
def cyclicalQueries(W, m):
    # Return the list of answers to all queries of type 4. Take the query information from standard input.
    c = Cycle(W)
    res = []
    
    for time in range(m):
        Q = input().split()
        if len(Q) == 2:
            Q.append(0)
        q, x, w = list(map(int, Q))
        x-=1
        prnt = True
        if q==1:
            #add new to far
            _, node = c.findFar(x)
            node.addToMax(w, time)
        elif q==2:
            #add new to x
            node = c.nodes[x]
            node.addNew(w, time)
        elif q==3:
            #remove far
            _, node = c.findFar(x)
            node.removeMax()
        else:
            #print dist
            dist, node = c.findFar(x)
            res.append(dist)
            prnt = False
            
        #if prnt:
        #    c.print()
        
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    m = int(input())

    result = cyclicalQueries(w, m)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
