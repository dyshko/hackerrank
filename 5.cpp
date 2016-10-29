#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/* This function calculates (a^b)%MOD */
long long pow(long long a, long long b, long long MOD) {
long long x = 1, y = a;
    while(b > 0) {
        if(b%2 == 1) {
            x=(x*y);
            if(x>MOD) x%=MOD;
        }
        y = (y*y);
        if(y>MOD) y%=MOD;
        b /= 2;
    }
    return x;
}
 
long long modInverse(long long a, long long m) {
    return pow(a,m-2,m);
}

const long long M = 1000000007;

//C_a^b (b < a/2)
long long binmod(long long a, long long b)
{
    long long u = 1;
    long long d = 1;
    for (long long i = a - b + 1 ; i <= a; i++)
    {
        u = (u * i)%M;
    }
    for (long long i = 1; i <= b; i++)
    {
        d = (d * i)%M;
    }
    return (u * modInverse(d,M))%M;
    
}

int main() {
    
    int T;
    cin>>T;
    for (int i = 0 ; i < T; i++)
    {
        int n,m;
        long long acalc, bcalc;
        cin>>n>>m;
        acalc = m + n - 2;
        bcalc = ((m - 1) < (n-1))?(m - 1):(n-1);
        cout<<binmod(acalc, bcalc)<<endl;
    }
    return 0;
}
