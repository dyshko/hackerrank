#!/bin/python3
import math
import sys

A,B,C,D = input().strip().split(' ')
A,B,C,D = [int(A),int(B),int(C),int(D)]

A, B, C, D = sorted([A,B,C,D])

MAX = max(A,B,C,D)
cst = 2**(math.floor(math.log(MAX,2))+1)

dicAB = [[0]*cst for i in range(B+1)]
dicCD = [[0]*cst for i in range(C+1)]


for i in range(1,A+1):
    for j in range(i, B+1):
        dicAB[j][i^j]+=1


        
for i in range(1, C+1):
    for j in range(i, D+1):
        dicCD[i][i^j]+=1

for sep in range(C, 1, -1):
    for val in range(cst):
        dicCD[sep-1][val]+=dicCD[sep][val]
        
res0 = 0
for val in range(cst):
    res0 += sum([dicAB[sep][val]*dicCD[sep][val] for sep in range(1,B+1)])

def ssq(x, y):
    s1 = (y*(y+1)*(2*y + 1))//6
    s2 = ((x-1)*((x-1)+1)*(2*(x-1) + 1))//6
    return s1 - s2

def sm(x, y):
    return (y*(y+1))//2 - ((x-1)*x)//2
    
total = 0
for i in range(1, A+1):
    c1 = (C+1)*(2*(D+1) - (C+1) + 1)
    c2 = -2*(D+1) - 1
    s = (B - i + 1)*c1 + sm(i, B)*c2 + ssq(i,B)
    total+= s//2
    
#total = 0
#for i in range(1, A+1):
#    for j in range(i, B+1):
#        total+=((C-j + 1)*(D-j + 1) - ((C-j + 1)*(C-j))//2)

#print(dicAB, dicCD, total)
    
res = total - res0
print(res)
