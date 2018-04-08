LOST = -1000000000000000

def totpow(S):
    CC = 1
    TS = 0
    for i in range(len(S)):
        if S[i] == 'C':
            CC*=2
        else:
            TS+=CC
    return TS

#Diff = Pow(S) - D
def foo(S, D):
    Pow = totpow(S)
    n = len(S)
    if n==0:
        if Pow <= D:
            return 0
        else:
            return LOST

    xc = len([x for x in S if x == 'C'])
    if xc == 0:
        return foo("", D - n)

    #num of right C
    nrc = 0
    for i in range(n):
        if S[n-i-1] == 'C':
            nrc+=1
        else:
            break

    if (nrc > 0):
        return foo(S[:n-nrc], D)

    nrs = 0
    for i in range(n):
        if S[n - i - 1] == 'S':
            nrs+=1
        else:
            break

    if D >= Pow - nrs*(2**(xc-1)):
        j = 0
        while D<Pow - j*(2**(xc-1)):
            j+=1
        return j
    else:
        return nrs + foo(S[:n-nrs-1]+nrs*'S', D)
        

T = int(input())
for tc in range(T):
    D, S = input().split()
    D = int(D)
    res = foo(S, D)
    if (res < 0):
        res = "IMPOSSIBLE"
    print("Case #"+str(tc+1)+": " + str(res))
