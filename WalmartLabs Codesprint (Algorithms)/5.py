MOD = 1000000007

memo = {}

def F(n):
    if n == 0:
        return 0
    if n not in memo:
        memo[n] = F_act(n)
    return memo[n]

def F_act(n):
    v1, v2, v3 = 1, 1, 0  
    for rec in bin(n)[3:]:
        calc = (v2*v2) % MOD
        v1, v2, v3 = (v1*v1+calc) % MOD, ((v1+v3)*v2) % MOD, (calc+v3*v3) % MOD
        if rec == '1': v1, v2, v3 = (v1+v2) % MOD, v1, v2
    return(v2)  

q = int(input())
for _q in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    e_here = 0
    e_here_m1 = 0
    for i in range(n):
        e_here, e_here_m1 = ( F(a[i] + 1)*e_here + F(a[i])*(e_here_m1 + 1) ) % MOD, ( F(a[i])*e_here + F(a[i]-1)*(e_here_m1 + 1) ) % MOD
        total = (total + e_here)%MOD
    print(total)
        