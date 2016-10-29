P = 1000000007

import sys

def facmod(n):
    r = 1
    for i in range(1,n+1):
        r*=i
        r%=P
    return r

def invmod(n):
    return pow(n,P-2,P)

def binmod(n, k):
    return (facmod(n)*invmod( (facmod(k)*facmod(n-k))%P ))%P

def chose(n, k):
    return binmod(n +k - 1, k -1)

A,B,C,D = input().strip().split(' ')
A,B,C,D = [int(A),int(B),int(C),int(D)]

res = 0
if B==0 and D == 0:
    if A!=0 and C!=0:
        res = 0
    elif A==0 and C==0:
        res = 2
    else:
        res = 1
elif (B==D):
    res = chose(A,B)*chose(C,B+1) + chose(A,B+1)*chose(C,B)
elif B - D == 1:
    res = chose(A,B)*chose(C,B)
elif D - B == 1:
    res = chose(A,D)*chose(C,D)
else:
    res = 0
    
print(res%P)