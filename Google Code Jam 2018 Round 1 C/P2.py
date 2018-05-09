import sys

T = int(input())
for tc in range(T):
    N = int(input())

    prefs_h = [0]*(N)
    lols = set()
    for i in range(0,N):
        lols.add(i)
    
    for c in range(N):

        flavs = set(list(map(int, input().split()))[1:])

        for f in flavs:
            prefs_h[f]+=1

        inter = list(flavs.intersection(lols))
        #sys.stderr.write(str(inter) +'\n')
        
        if len(inter) == 0:
            #sys.stderr.write('printing -1\n')
            print(-1)
            sys.stdout.flush()
            continue

        inter.sort(key = lambda x: prefs_h[x])
        
        lols.remove(inter[0])

        print(inter[0])
        sys.stdout.flush()
