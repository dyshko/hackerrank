MOD = 1000000007

def invmod(v):
    return pow(v, MOD-2, MOD)

cat = [1]*2001
for i in range(1,2001):
    cat[i] = (cat[i-1]*(2*i-1)*(2*i)*invmod(i*(i+1)) ) %MOD
    #2n! / n! n+1!
    
res = [1]*2001
for i in range(1,2001):
    res[i] = (res[i-1] + cat[i])%MOD

t = int(input())
for _t in range(t):
    n = int(input())
    if n%2==1:
        print(0)
    else:
        print(res[n//2]-1)