T = int(input())
for tc in range(T):

    S = int(input())
    L = {}
    R = {}

    
    for i in range(S):
        d, a, b = map(int, input().split())
        if d+a in L:
            L[d+a].append(i)
        else:
            L[d+a] = [i]

        if d-b in R:
            R[d-b].append(i)
        else:
            R[d-b] = [i]

    cnt = {}

    seen = {}

    for x in L:
        for y in R:
            mix = list(set(L[x] + R[y]))
            mix.sort()

            if str(mix) in seen:
                continue
            else:
                seen[str(mix)] = 0
            #print(L[x], R[y], list(set(L[x] + R[y])))

            maxTot = 0
            #find contig
            #print(mix)
            for i in range(0,len(mix)):
                maxC = 1
                for j in range(i+1, len(mix)):
                    if mix[j] != mix[j-1] + 1:
                        break
                    else:
                        maxC+=1
                maxTot = max(maxTot, maxC)
            if maxTot in cnt:
                cnt[maxTot]+=1
            else:
                cnt[maxTot]=1

    mx = max(cnt.keys())
    
    
    print("Case #"+str(tc+1)+": " + str(mx) + " " + str(cnt[mx]))
