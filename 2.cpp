#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define ll long long
#define ld long double

ll inline multmod(ll x, ll y, ll p)
{
    return ((x%p)*(y%p))%p;
}

inline ll powmod(ll x, ll pow,ll p)
{
    if (pow>1)
    {
        return multmod(powmod(
            multmod(x,x,p),pow/2,p
            ), powmod(x,pow%2,p),p);
    }
    if (pow == 1) return x%p;
    if (pow == 0) return 1;
}

ld front(ld x)
{
    return x - floor(x);
}

int main() {
    
    ll T;
    cin>>T;
    for (ll i=0;i<T;i++)
    {
        ll N;
        ll K;
        cin>>N>>K;
        ld d=pow((double)10, (double)(front((N-1)*(0.30102999566398119521373889472449L))-1));
        
        const ld p10d=(ll) pow(10,K);
        const ll p10=(ll)p10d;
        
        ll last=powmod(2,N-1,p10);
        ll f=(ll) (d*p10d);
        cout<<f+last<<"\n";
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
