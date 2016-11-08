MOD = 998244353

def inv(x):
    return pow(x, MOD-2, MOD)

n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if k>=n-1:
    print(0)
else:
    
    #calculate factorials
    fac = [1]*(k+1)
    for i in range(2,k+1):
        fac[i] = (fac[i-1]*i)%MOD
        
    # wj coefficients
    w = [1]*(k+1)
    for j in range(k+1):
        w[j] = (fac[j]*fac[k-j]*(-1)**(k-j))%MOD
    res = -1
    for shift in range(n):
        interOK = True
        for i in range(k+1, n):
            #topsum
            ts = 0
            #botsum
            bs = 0
            for j in range(k+1):
                v = inv(w[j]*(i-j))
                ts += v*(a[j] - b[(j+shift)%n])
                bs += v
                ts%=MOD
                bs%=MOD
            #print(shift, i,(bs*(a[i] - b[(i+shift)%n]))%MOD, ts)
            if (bs*(a[i] - b[(i+shift)%n]))%MOD != ts:
                #interpolation not ok
                interOK = False
                break
            #print()
        if interOK:
            res = shift
            break
    print(res)