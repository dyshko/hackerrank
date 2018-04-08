T = int(input())
for tc in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    even = [a[i] for i in range(0, n, 2)]
    odd  = [a[i] for i in range(1, n, 2)]
    even.sort()
    odd.sort()
    #merge
    for i in range(0, n, 2):
        a[i] = even[i//2]
        if i+1 < n:
            a[i+1] = odd[i//2]
    res = -1
    #print(a)
    for i in range(n-1):
        if a[i] > a[i+1]:
            res = i
            break
    if res < 0:
        res = "OK"
    print("Case #" + str(tc+1) + ": " + str(res))
            
        
    
