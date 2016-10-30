#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <string>
using namespace std;

string getString(int d)
{
    switch (d)
    {
        case 0: return "UP";
        case 1: return "RIGHT";
        case 2: return "DOWN";
        case 3: return "LEFT";
        default:return "";
    }
    return "";
}

void getVec(int& h, int& v, int d)
{
    switch (d)
    {
        case 0: h=0; v=-1;break;
        case 1: h=1; v=0; break;
        case 2: h=0; v=1; break;
        case 3: h=-1; v=0;break;
        default: break;
    }
}

bool isvalid(char t[][10], int x, int y,int n,int m, int d)
{
    int hor=0;
    int ver=0;
    getVec(hor,ver,d);
    if (((x+2*ver)>=n) || ((x+2*ver) <0)) return false;
    if (((y+2*hor)>=m) || ((y+2*hor) <0)) return false;
    if (t[x][y]=='.')
        if (t[x+ver][y+hor]=='.')
            if (t[x+2*ver][y+2*hor]=='-') return true;
    return false;
}

void move(char t[][10], int x, int y, int d)
{
    int hor=0;
    int ver=0;
    getVec(hor,ver,d);
    t[x][y]='-';
    t[x+ver][y+hor]='-';
    t[x+2*ver][y+2*hor]='.';
}


int main() {
    int N,M;
    cin>>M>>N;
    char T[10][10];
    for (int i=0;i<M;i++)
        for (int j=0;j<N;j++) cin>>T[i][j];
    int count=0;
    int nomoves=0;
    string st="";
    while (!nomoves)
    {
        nomoves=1;
        for (int i=0;i<N;i++)
        {
            for (int j=0;j<M;j++)
            {
                for (int d=0;d<4;d++)
                {
                    if (isvalid(T,i,j,N,M,d))
                    {
                        move(T,i,j,d);
                        nomoves=0;
                        count++;
                        st+=to_string(j);
                        st+=" "; st+=to_string(i);
                        st+=" "; st+=getString(d);
                        st+="\n";
                    }
                }
            }
        }
    }
    cout<<count<<"\n"<<st;
    return 0;
}