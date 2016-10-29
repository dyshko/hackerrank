#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define llong long
const llong MOD = 1000000007; 

llong phi(llong n)
{
    if (n == 1)
        return 1;
    llong out = n;
    if (n % 2 == 0) {
        out -= out / 2;
        do
            n /= 2;
        while (n % 2 == 0);
    }
    for (llong i = 3; i * i <= n; i += 2)
        if (n % i == 0) {
            out -= out / i;
            do
                n /= i;
            while (n % i == 0);
        }
    //
    if (n > 1)
        out -= out / n;
    return out % MOD;
}

llong n(llong max , llong k)
{
    return (max/k)% MOD;
}

int main() {
    int T;
    cin>>T;
    for (int t = 0 ; t < T; t++)
    {
        int K;
        int num[500];
        cin>>K;
        llong Min = 100000;
        for (int k = 0 ; k < K; k++)
        {
            cin>>num[k];
            if (num[k] < Min) Min = num[k];
        }
        
        llong res = 0;
        for (int i = 1; i <= Min; i++)
        {
            llong pres = 1;
            for (int j = 0; j < K; j++)
            {
                pres = (pres * n(num[j],i))%MOD;
            }
            res += (pres * phi(i)) % MOD;
        }
        cout<<(res%MOD)<<endl;
    }
    return 0;
}
