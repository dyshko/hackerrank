t = int(input())

for _t in range(t):
    n, k, b = list(map(int, input().split()))
    
    res = []
    
    v = (2*n + b - b*b)//(2*b)
    sm = ((2*v - 1 + (b+1))*(b+1))//2
    
#    print(v, sm, 555)
    if v <= 0 or ( v + b - 1 > k and (2*n + b - b*b)%(2*b)==0) or ( v + b - 1 >= k and (2*n + b - b*b)%(2*b)!=0):
        res = [-1]
    else:
        res = [x for x in range(v, v+b+1, 1) if x!=sm-n]
    print(" ".join([str(x) for x in res]))