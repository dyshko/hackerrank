def score_zero(x):
    if x<100:
        return 0
    else:
        return score_nonzero(x)

def score_nonzero(x):
    l = x//100
    m = (x - l*100)//10
    r = x%10
    if (l<m and m>r) or (l>m and m<r):
        return 1
    return 0

val_zero = [0]*1000
val_nonzero = [0]*1000
f_zero   = [0]*1000
f_nonzero = [0]*1000
for i in range(1,1000):
    val_zero[i] = score_zero(i)
    f_zero[i] = f_zero[i-1] + val_zero[i]
    val_nonzero[i] = score_nonzero(i)
    f_nonzero[i] = f_nonzero[i-1] + val_nonzero[i]

def foo(A):
    A = str(A)
    n = len(A)
    if n<3:
        return 0
    res = 0
    for i in range(n-2):
        L = 0
        R = 0
        if i > 0:
            L = int(A[:i])
        M = int(A[i:i+3])
        if i<n-3:
            R = int(A[i+3:])
        if M==0:
            if L==0:
                res += 0
            else:
                res += (f_zero[999] + f_nonzero[999]*(L-1))*(10**(n-i-3))
        else:
            if L==0:
                res += (f_zero[M-1])*(10**(n-i-3)) + val_zero[M]*(R+1)
            else:
                res += ( f_zero[999] +f_nonzero[999]*(L-1) + f_nonzero[M-1])*(10**(n-i-3)) + val_nonzero[M]*(R+1)
    return res
        

a = int(input())
b = int(input())
    
print(foo(b) - foo(a-1))