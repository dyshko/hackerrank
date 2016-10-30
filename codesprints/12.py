T = int(input())
for t in range(T):
    n = int(input())
    h = list(map(int, input().split()))
    h.sort()
    if n==1:
        res = max(2, h[0])
    else:
        res = 0
        s = 0
        for i in range(n, 0, -1):
            if s > h[i-1]*i:
                res = s*(i+1)
                break
            s+=h[i-1]
    print(res)