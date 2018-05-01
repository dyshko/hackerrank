import math

#needed to cross 0.5
def to05(x, N):
    #print(x, N)
    delta = 0.5 - (100*x/N)%1
    if delta <= 0:
        #print("111",delta)
        return 0

    if delta >= 100/N:
        #print("222", int(math.ceil(N*delta/100)))
        return int(math.ceil(N*delta/100))
    else:
        res = 0
        while 0.5 - (100*x/N)%1 > 0:
            #print(0.5 - (100*x/N)%1)
            x+=1
            res += 1
        return res

T = int(input())
for tc in range(T):
    
    N, L = list(map(int, input().split()))
    A = list(map(int, input().split()))

    left = N - sum(A)
    A += [0]*left

    if N in [1, 2, 4, 5, 10, 20, 25, 50, 100]:
        print("Case #"+str(tc+1)+": " + str(100))
        continue

    A.sort(key = lambda x: to05(x, N))

    

    i = 0
    while left > 0:
        val = to05(A[i],N)
        #print(A[i], val, A, [to05(x, N) for x in A])
        while val > 0 and left > 0:
            if val <= left:
                A[i] += val
                left -= val
            break
        i+=1
        if i >= len(A) and left > 0:
            A[i-1] = left
            break

    res = 0
    for a in A:
        pr = 100*a/N
        if pr%1 >= 0.5:
            res += int(math.ceil(pr))
        else:
            res += int(pr)
    #print(A)
    
    print("Case #"+str(tc+1)+": " + str(res))
