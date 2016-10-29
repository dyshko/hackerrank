#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define MOD 1000000007

int a[20];
int n;
int t[100];
int S;
long long cnt[300000] {0};
long long cntprev[300000] {0};
long long cntaux[15][300000] {{0}};
long long cntauxprev[15][300000] {{0}};

void fill(int K){
    //
    fill(cnt, cnt+300000, 0);
    fill(cntprev, cntprev+300000, 0);
    fill(cntaux[0], cntaux[14]+300000, 0);
    fill(cntauxprev[0], cntauxprev[14]+300000, 0);
    //
    
    cntprev[0]=1;
    for (int c = 1; c<=S; ++c) cntprev[c]=0;
    for (int c = 0; c <= S; ++c) cntauxprev[0][c]=cntprev[c];
    for (int c = S+1; c<=2*S; ++c) cntauxprev[0][c] = 0;
    
    for (int j = 0; j<=K; ++j){
        for (int c = 0; c <= S; ++c) cntaux[0][c] = cntprev[c];
        for (int c = S+1; c<=2*S; ++c) cntaux[0][c] = 0;
        
        for (int i = 1; i <= n; ++i){
            for (int c = 0; c <= a[i] - 1; ++c) cntaux[i][c] = cntaux[i-1][c];
            for (int c = a[i]; c<=2*S; ++c)     cntaux[i][c] = (cntaux[i-1][c] + cntaux[i-1][c- a[i]])%MOD;
        }
        
        for (int c = 0; c <=S; ++c) cnt[c] = cntaux[n][2*c + t[j]];
        
        swap(cnt, cntprev);
        swap(cntaux, cntauxprev);
    }
}

int F(long long N){
    if (N==0) return 1;
    int K = floor(log2(N));
   // cout<<K<<endl;
    for (int i = 0; i < K+1; ++i){
        t[i] = N%2;
        N/=2;
    }
    S = 0;
    for (int i = 1; i <= n; ++i){
        S+=a[i];
    }
    fill(K);
    return cntprev[0]%MOD;
}

int main() {
    cin>>n;
    for(int i = 1; i <= n; ++i){
        cin>>a[i];
    }
    a[n+1] = 1;
    n+=1;
    long long L, R;
    cin>>L>>R;
    int res = (F(R) - F(L-1))%MOD;
    if (res < 0) res+=MOD;
    cout<<res;
    return 0;
}
