MOD = 1000000007

kmax = 201
nmax = 101

# n blocks, exactly k changes
cat = [[0]*kmax for i in range(nmax)]

cat[0][0] = 1
for i in range(1, nmax):
    cat[i][0] = 0
for i in range(1, nmax):
    cat[i][1] = 1
for i in range(1, kmax):
    cat[0][i] = 0
for i in range(0, kmax):
    cat[1][i] = 0
cat[1][1] = 1


for n in range(2,nmax):
    for k in range(2,kmax):
        if 2*n<k:
            cat[n][k] = 0
        else:
            for i in range(1,n-1):
                for j in range(k):
                    cat[n][k] += cat[i][j]*cat[n-i-1][k-j-1]
            cat[n][k] += cat[n-1][k-2]
            cat[n][k] += cat[n-1][k]
            cat[n][k]%=MOD
    

q = int(input())
for _q in range(q):
    n, k = list(map(int, input().split()))
    if n%2!=0:
        print(0)
    else:
        print(sum([cat[n//2][i] for i in range(k, kmax)])%MOD)
    