#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
#define long long long
long inline factmod(long x, long p)
{
    if (x == 0) return 1;
    if (x == 1) return 1;
    else return ((x%p)*(factmod(x-1,p))%p);
}

long inline multmod(long x, long y, long p)
{
    return ((x%p)*(y%p))%p;
}

inline long powmod(long x, long pow,long p)
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

//compute x^(p-2) mod p
inline long inversemod(long x, long p)
{
    return powmod(x, p-2, p);
}

int main() {
    
    string c;
    getline(cin,c);
    int n=c.length();
    const int N=256;
    int counter[N];
    for (int i=0;i<N;i++)
    {
        counter[i]=0;
    }
    for (int i=0;i<n;i++)
    {
        counter[c[i]]++;
    }
    long const p=1000000007;
    long ch=1;
    long zn=1;
    long s=0;
    for (int i=0;i<N;i++)
    {
        zn=multmod(zn,factmod(counter[i]/2,p),p);
        s+=counter[i]/2;
    }
    ch = factmod(s,p);
    long res=multmod(ch, inversemod(zn,p),p);
    cout<<res;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
