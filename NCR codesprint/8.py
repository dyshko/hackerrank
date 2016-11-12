def line_intersection(p1,p2,p3,p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    bx = float(x2) - float(x1)
    by = float(y2) - float(y1)
    dx = float(x4) - float(x3)
    dy = float(y4) - float(y3)
    b_dot_d_perp = bx*dy - by*dx
    if b_dot_d_perp == 0:
        return None,None
    cx = float(x3) - float(x1)
    cy = float(y3) - float(y1)
    t = (cx*dy - cy*dx) / b_dot_d_perp
    return x1 + t*bx, y1 + t*by

def _left_right(p1, p2, p3):
    '''
    is (x3,y3) to the 'left' or 'right' of the line from (x1,y1) to (x2,y2) ?
    '''
    dx2,dy2 = p2[0]-p1[0], p2[1]-p1[1]
    dx3,dy3 = p3[0]-p1[0], p3[1]-p1[1]
    return (dx2 * dy3 - dx3 * dy2) > 0

def clip(poly1, poly2):
    N2 = len(poly2)
    # clip by each edge in turn.
    for j in range(N2):
        # target "left_right" value
        clip1 = poly2[j]
        clip2 = poly2[(j+1)%N2]
        LRinside = _left_right(clip1, clip2, poly2[(j+2)%N2])
        # are poly vertices inside or outside the clip polygon?
        isinside = [_left_right(clip1, clip2, p) == LRinside
                    for p in poly1]
        # the resulting clipped polygon
        clipped = []
        N1 = len(poly1)
        for i in range(N1):
            S = poly1[i]
            E = poly1[(i+1)%N1]
            Sin = isinside[i]
            Ein = isinside[(i+1)%N1]
            if Ein:
                if not Sin:
                    clipped.append(line_intersection(clip1, clip2, S, E))
                clipped.append(E)
            else:
                if Sin:
                    clipped.append(line_intersection(clip1, clip2, S, E))
        poly1 = clipped
    return poly1

def triarea(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/float(2)

def polyarea(p):
    n = len(p)
    if n<3:
        return 0
    area = 0
    for i in range(1,n-1):
        area+=triarea(p[0][0],p[0][1],p[i][0],p[i][1],p[i+1][0],p[i+1][1])
    return area
    
    

n = int(input())
tris = [None]*n
for i in range(n):
    x1, y1, x2, y2, x3, y3 = list(map(int,input().split()))
    if x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2) < 0:
        tris[i] = [ [x1,y1], [x2, y2], [x3, y3] ]
    else:
        tris[i] = [ [x1,y1], [x3, y3], [x2, y2] ]
        
dp = {}
dp_area = {}

rng = list(range(n))
    
total = 0
for i in range(n):
    dp[tuple([i])] = tris[i]
    dp_area[tuple([i])] = polyarea(tris[i])
    total+=dp_area[tuple([i])]

import itertools

#print(clip(tris[0], tris[1]))
#print(clip(tris[1], tris[0]))
#print(tris[2], tris[1])

if n<=20:
    for l in range(2,n+1):
        coef = (-1)**(l+1)
        for I in itertools.combinations(rng, l):
        #print(tris[I[0]], dp[I[1:]])
            if dp_area[I[1:]] > 0.00000001:
            #print(tris[I[0]], dp[I[1:]])
                pI = clip(tris[I[0]], dp[I[1:]])
                dp[I] = pI
                dp_area[I] = polyarea(pI)
                total+=dp_area[I]*coef
            else:
                dp_area[I] = 0
                dp[I] = []

print(total)
    
    