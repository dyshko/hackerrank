g = int(input())
for i in range(g):
    l, r, k = list(map(int,input().split()))
    if 1<=k%(l+r)<=r:
        print("Alice")
    else:
        print("Bob")