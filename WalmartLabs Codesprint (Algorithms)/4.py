dict = {}

def dist(a,b):
    if (a,b) not in dict:
        dict[(a,b)] = dist_act(a,b)
    return dict[(a,b)]

def dist_act(a, b):
    a = bin(a)[2:]
    b = bin(b)[2:]
    i = 0
    while i < min(len(a), len(b)) and a[i]==b[i]:
        i+=1
    return len(a) + len(b) - 2*i
    

n, m, q = list(map(int, input().split()))
food_loc = [ [] for i in range(m) ]
for i in range(m):
    food_loc[i] = list(map(int, input().split()))[1:]

res = 0
cur = 1

for _q in range(q):
    fi, pk = list(map(int, input().split()))
    mini = 100000
    #arg = 0
    for f_loc in food_loc[fi-1]:
        if dist(f_loc, cur) + dist(f_loc, pk) < mini:
            mini = dist(f_loc, cur) + dist(f_loc, pk)
    #        arg = f_loc
    #print("from",cur,"via",arg,"to",pk,"dist=",mini)
    res+=mini
    cur = pk

print(res)