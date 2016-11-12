def foo(a, n0, m0, n, m):
    if n <= n0 or m <= m0:
        return []
    res = []
    c = m0
    r = n
    while (r>n0):
        r-=1
        res.append(a[r][c])
    if m-m0>1:
        c = m0
        while (c<m-1):
            c+=1
            res.append(a[n0][c])
        if n-n0>1:
            while (r<n-1):
                r+=1
                res.append(a[r][m-1])
            c=m-1
            while (c>m0+1):
                c-=1
                res.append(a[n-1][c])
    return res

n , m = list(map(int, input().split()))
a = [ None ]*n
for i in range(n):
    a[i] = list(input())

n0 = 0
m0 = 0
res = []
while n > n0 and m > m0:
    res+=foo(a, n0, m0, n, m)
    #print(res)
    n0+=1
    m0+=1
    n-=1
    m-=1
    
s = "".join(res)
l = [x for x in s.split('#') if x!=""]
print(len(l))

