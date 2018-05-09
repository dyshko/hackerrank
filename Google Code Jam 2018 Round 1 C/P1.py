import itertools
import random

def hwords(hist, L):
    words = []
    for j in range(L):
        words.append("".join(hist[j].keys()))
    return words

T = int(input())
for tc in range(T):
    N, L = map(int, input().split())
    words = {}
    hist = [{} for i in range(L)]
    for i in range(N):
        s = input()
        words[s] = 0
        for j in range(L):
            hist[j][s[j]] = 0

    res = "-"
    cnt = 1
    for j in range(L):
        cnt*=len(hist[j])
    #print(cnt)

    if cnt < 10000:
        #print(hwords(hist, L))
        for w in itertools.product(*hwords(hist, L)):
            wrd = "".join(w)
            #print(wrd)
            if wrd not in words:
                res = wrd
                break
    else:
        while True:
            w = ""
            for j in range(L):
                rc = random.choice(list(hist[j].keys()))
                w+=rc
            if w not in words:
                res = w
                break
        
    print("Case #"+str(tc+1)+": " + res)
