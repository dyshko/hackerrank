def foo_h(a, i, j, n, m, k):
    if j+k > m:
        return False
    for ind in range(j+1, j+k):
        if a[i][ind]!=a[i][j]:
            return False
    return True

def foo_v(a, i, j, n, m, k):
    if i+k > n:
        return False
    for ind in range(i+1, i+k):
        if a[ind][j]!=a[i][j]:
            return False
    return True

def foo_d(a, i, j, n, m, k):
    if i+k > n or j+k >m:
        return False
    for ind in range(1, k):
        if a[i+ind][j+ind]!=a[i][j]:
            return False
    return True

def play(a, n, m, k):
    xwin = False
    owin = False
    for i in range(n):
        for j in range(m):
            if foo_h(a, i, j, n, m, k) or foo_v(a, i, j, n, m, k) or foo_d(a, i, j, n, m, k):
                if a[i][j]=='X':
                    xwin = True
                elif a[i][j]=='O':
                    owin = True
                    #print(i,j,foo_h(a, i, j, n, m, k),foo_v(a, i, j, n, m, k),foo_d(a, i, j, n, m, k))
            if xwin and owin:
                return [xwin, owin]
    return [xwin, owin]
    
g = int(input())

for _g in range(g):
    n, m, k = list(map(int, input().split()))
    a = [None]*n
    for i in range(n):
        a[i] = input()
    xwin, owin = play(a,n,m,k)
    if xwin and not owin:
        print("LOSE")
    elif not xwin and owin:
        print("WIN")
    else:
        print("NONE")