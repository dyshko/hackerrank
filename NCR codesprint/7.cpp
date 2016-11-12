#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

bool bpm(int bpGraph[], int u, bool seen[], int matchR[], int M, int N)
{
    for (int v = 0; v < N; v++)
    {
        if (bpGraph[u*N + v]==1 && !seen[v])
        {
            seen[v] = true;
            if (matchR[v] < 0 || bpm(bpGraph, matchR[v], seen, matchR, M, N))
            {
                matchR[v] = u;
                return true;
            }
        }
    }
    return false;
}
 
int maxBPM(int bpGraph[], int M, int N)
{
    
    int matchR[N];
    memset(matchR, -1, sizeof(matchR));
 
    int result = 0;
    for (int u = 0; u < M; u++)
    {
        bool seen[N];
        memset(seen, 0, sizeof(seen));
        if (bpm(bpGraph, u, seen, matchR, M, N))
            result++;
    }
    return result;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int area[120000];
    int p;
    cin>>p;
for (int _p =0; _p < p;++_p){
    int r, c, n, m;
    cin>>r>>c>>n>>m;
    memset(area, 0, r*c);
    for (int day = 0; day < n; ++day){
        int x1, y1, x2, y2;
        cin>>x1>>y1>>x2>>y2;
        for (int i = x1; i<=x2; ++i){
            for (int j = y1; j <= y2; ++j){
                area[i*c+j]++;
            }
        }
        
    }
    
    for (int i=0; i<r; ++i){
            for (int j=0; j < c; ++j){
                if (area[i*c+j]>=m) area[i*c+j] = 1;
                else area[i*c+j] = 0;
            }
    }           
    cout<<maxBPM(area, r, c)<<endl;
}
    return 0;
}



 


