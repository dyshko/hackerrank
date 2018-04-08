import decimal
decimal.setcontext(decimal.Context(prec=36))

T = int(input())

def vp(v1, v2):
    return (  v1[1]*v2[2] - v1[2]*v2[1],
             -v1[0]*v2[2] + v1[2]*v2[0],
              v1[0]*v2[1] - v1[1]*v2[0])

D0 = decimal.Decimal(0.0)
D1 = decimal.Decimal(1.0)
D2 = decimal.Decimal(2.0)
D3 = decimal.Decimal(3.0)

def printShift(v):
    print(" ".join(["{0:.20f}".format(x/D2) for x in v]))
    #print("Size:", (v[0]**2 + v[1]**2 + v[2]**2).sqrt())

def ang(v1, v2):
    res = D0
    for i in range(3):
        res+=v1[i]*v2[i]
    print(res)
for tc in range(T):
    A = decimal.Decimal(input())

    v1 = None
    v2 = None
    if A > D3.sqrt():
        A = D3.sqrt()
    if A < D1:
        A = D1


    if ( A > D2.sqrt() ):
        y1 = ( D2*A + (D2*(D3 - A**2)).sqrt() ) / decimal.Decimal(6.0)
        rt = (D1 - y1**2).sqrt()
        v1 = ( rt , y1, 0.0 )
        v2 = ( -(y1**2)/rt, y1, (D1 - D2* (y1**2)).sqrt() / rt )
    elif (A > 1):
        y1 = ( A + (D2 - A**2).sqrt() ) / D2
        
        y2 = (D1 - y1**2).sqrt()
        v1 = ( y2 , y1, D0 )
        v2 = ( -y1, y2, D0 )
    else:
        v1 = (D1, D0, D0)
        v2 = (D0, D1, D0)
        
    v3 = vp(v1, v2)

    #ang(v1,v2)
    #ang(v1,v3)
    #ang(v2,v3)

    #print("Area", abs( v1[0]*v2[2] - v1[2]*v2[0]) + abs(v1[1]) + abs(v2[1]))

    print("Case #" + str(tc+1) + ":")
    printShift(v1)
    printShift(v2)
    printShift(v3)
