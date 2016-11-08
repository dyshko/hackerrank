n, m = list(map(int, input().split()))

s = list(map(int, input().split()))

s = [x for x in s if n%x==0]
s.sort()
m = len(s)
dp = {}

def foo(n):
    if n not in dp:
        dp[n] = foo_act(n)
    return dp[n]

def foo_act(n):
    if n==0:
        return False
    for x in s:#no even entries here
        if n%x==0:
                val = foo(n//x)
                if not val:
                    return True
    return False

iseven = False
for x in s:
    if x%2==0:
        iseven = True
        break

if iseven:
    print("First")
else:
    print(foo(n)*"First" + (not foo(n))*"Second")