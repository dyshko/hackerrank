#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define ull unsigned long long

ull fac(ull n){
    if (n==0){
        return 1;
    }
    else{
        return n*fac(n-1);
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    cin>>n;
    int p[n];
    for (int i=0; i<n; ++i){
        cin>>p[i];
    }
    if (is_sorted(p, p+n)){
        cout<<"0.000000";
        return 0;
    }
    sort(p, p+n);
    ull res = fac((ull)n);
    int t=1;
    for (int i = 1; i < n; ++i){
        if (p[i]==p[i-1]) ++t;
        else
        {
            res/= fac((ull)t);
            t = 1;
        }
    }
    res /= fac((ull)t);
    cout<<res<<".000000";
    return 0;
}
