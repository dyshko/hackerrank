#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int MOD = 1000000009;
    int n;
    cin>>n;

    int res[201][101] = {0};
    int dist[101] = {0};
    int a;
    for (int i; i < n; ++i){
        cin>>a;
        for (int d = a - 100; d < a; ++d){
            res[d+100][a] = (res[d+100][a] + res[d+100][a-d]) % MOD;
        }
        for (int j = 1; j<=100; ++j){
            res[a-j + 100][a] = (res[a-j + 100][a] + dist[j]) % MOD;
        }
        dist[a]+=1;
    }
    
    int ans = 0;
    for (int d = -100; d <= 100; ++d){
        for (int e = 1; e<=100; ++e){ 
            ans = (ans + res[d+100][e]) % MOD;
        }
    }
    cout<<(ans + n + 1)% MOD; 
    return 0;
}
