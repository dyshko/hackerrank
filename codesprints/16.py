#code from the internet
def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
#end code from the internet


n = int(input())
a = list(map(int, input().split()))

prime_0 = primes(n+1)
ppowers = {}
ppowers[1]=1
for p in prime_0:
    pp = p
    while pp<=n:
        ppowers[pp]=p
        pp*=p

#print(ppowers)
        
divisors = [[] for i in range(n+2)]
for i in range(2,n+1):
    for j in range(2,((n+1)//i)+1):
        divisors[j*i].append(i)
        
def first(a, n):
    for k in range(n-1, -1, -1):
        if a[k] > k:
            return False
        elif 0<=a[k]<=k:
            for m in divisors[k+1]:
                if a[m-1]==-1:
                    a[m-1]=a[k]%m
                else:
                    if (a[m-1]-a[k])%m!=0:
                        return False
    return True

def second(a,n):
    res = 1
    MOD = 1000000007
    for k in range(1,n):
        if a[k]==-1:
            if k+1 in ppowers:
                res*=ppowers[k+1]
            """
            fac = factor(k+1)
            if len(fac)==1:
                res*=fac[0][0]
            """
            res%=MOD
    return res

if (first(a,n)):
    print(second(a,n))
else:
    print(0)