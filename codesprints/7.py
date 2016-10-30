X = 1000000007

def gcd(a,b):
    if b > a:
        return gcd(b,a)
    r = a%b
    if r == 0:
        return b
    return gcd(r,b)

def mul(A, B):
    a, b, c = A
    d, e, f = B
    return (a*d + b*e)%X, (a*e + b*f)%X, (b*e + c*f)%X

def pow(A, n):
    if n == 1:     return A
    if n & 1 == 0: return pow(mul(A, A), n//2)
    else:          return mul(A, pow(mul(A, A), (n-1)//2))

def fib(n):
    if n < 2: return n
    return pow((1,1,0), n-1)[0]


N = int(input())
res = int(input())
for i in range(N-1):
    res = gcd(res,int(input()))
print(fib(res)%X)