T = int(input())
for t in range(T):
    n = int(input())
    A = list(map(int,input().split()))
    s = 0
    f = 0
    dead = -1
    pos = 0
    wasdeath = 0
    for i in range(n):
        if A[i]>=0:
            s+=A[i]
        else:
            if s >= -A[i]:
                s+=A[i]
            else:
                #1st dead condition
                pos = i
                s+=A[i]
                wasdeath = 1
                break
    if wasdeath == 0:
        print("She did it!")
    else:
        B = [-x for x in A[:pos+1] if x<0]
        m = max(B)
        s += 2*m
        for i in range(pos+1, n):
            if A[i]>=0:
                s+=A[i]
            else:
                if s >= -A[i]:
                    s+=A[i]
                else:
                    dead = i+1
                    break
        if dead == -1:
            print("She did it!")
        else:
            print(dead)