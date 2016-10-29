n, m = list(map(int, input().split()))

def i2a(I,n):
    s = list(map(int,bin(I)[2:]))
    s = [0]*(n - len(s)) + s
    return s

def a2i(s):
    res = 0
    for i in range(n):
        res = (res<<1) | s[i]
    return res

def superset(I):
    res = []
    s = i2a(I,n)
    zpos = [i for i in range(n) if s[i]==0]
    zn = len(zpos)
    for i in range(2**zn):
        nums = i2a(i, zn)
        s1 = list(s)
        for j in range(zn):
            s1[zpos[j]] = nums[j]
        res+=[a2i(s1)]
    return res

def get_querries(I,querries):
    s = i2a(I,n)
    res = []
    for i in superset(I):
        res+=querries[i]
    return res

querries = [[] for i in range(2**n)]

for _q in range(m):
    q = input().split()
    if q[0]=='1':
        x = int(q[1])
        s = [int(c) for c in q[2]]
        i = a2i(s)
        querries[i] = [[1,x,_q]]
    elif q[0]=='2':
        x = int(q[1])
        s = [int(c) for c in q[2]]
        i = a2i(s)
        L = querries[i]
 
    #    if len(L)>0 and (L[len(L)-1][0]==2):
    #        x_old = L[len(L)-1][1]
    #        querries[i][len(L)-1] = [2,x^x_old,_q]
    #    else:
        querries[i].append([2,x,_q])
    else:
        s = [int(c) for c in q[1]]
        i = a2i(s)
  #      print(i, superset(i))
        L = get_querries(i, querries)
        if len(L)>0:
            L.sort(key = lambda x: x[2], reverse = True)
            res = 0
            for r in L:
                res^=r[1]
                if r[0]==1:
                    break
            print(res)
        else:
            print(0)