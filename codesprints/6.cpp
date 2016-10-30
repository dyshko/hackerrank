#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

typedef struct ss_
{
    int x;
    int y;
    int z;
    long long W;
    long long dW;
} uq;

int main() {
    
    int T;
    cin>>T;
    for (int t = 0 ; t < T; t++)
    {
        int N, M;
        cin>>N>>M;
        uq uqs[M];
        int counter_u = 0;
        string qw = "";
        for (int q = 0; q < M; q++)
        {
            cin>>qw;
            if (qw == "UPDATE")
            {
                cin>>uqs[counter_u].x>>uqs[counter_u].y>>uqs[counter_u].z>>uqs[counter_u].W;
                uqs[counter_u].dW = uqs[counter_u].W;
                for (int i = counter_u-1 ; i >= 0 ; i--)
                {
                    if ((uqs[i].x == uqs[counter_u].x)
                        &&(uqs[i].y == uqs[counter_u].y)
                        &&(uqs[i].z == uqs[counter_u].z))
                        {
                            uqs[counter_u].dW = uqs[counter_u].W - uqs[i].W;
                            break;
                        }
                }
                counter_u++;
            }
            else if (qw == "QUERY")
            {
                int x1,y1,z1,x2,y2,z2;
                long long sum = 0;
                cin>>x1>>y1>>z1>>x2>>y2>>z2;
                for (int i = 0; i < counter_u; i++)
                {
                    if ((uqs[i].x >= x1) && (uqs[i].x <= x2)
                        &&(uqs[i].y >= y1) && (uqs[i].y <= y2)
                        &&(uqs[i].z >= z1) && (uqs[i].z <= z2)) sum+=uqs[i].dW;
                }
                cout<<sum<<endl;
            }
        }
        

    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
