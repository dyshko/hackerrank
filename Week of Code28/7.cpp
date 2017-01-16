#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


typedef unsigned int int_t;
typedef unsigned long long_t;

const int_t MOD = 998244353;

vector<int_t> f;
long_t f_max;

void print_v(vector<int_t> v, long_t mx){
    if (v.size() < mx+1) cerr<<"ERROR";
    for (long_t i = 0; i <= mx; ++i){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}

int_t modinv(long_t b) {
  b %= MOD;
  long_t res = 1;
  int_t exp = MOD - 2;
  while (exp > 0) {
    if (exp & 1) res = (res * b) % MOD;
    b = (b * b) % MOD;
    exp >>= 1;
  }
  return res;
}

inline void mulmod(int_t& x, int_t y){
    long_t x0 = x;
    x = (int_t) ((x0*y)%MOD);
}

//x+=(y*z) mod MOD
inline void mulmodsum(int_t& x, int_t y, int_t z){
    long_t y0 = y;
    x = (int_t) ((x + (y0*z))%MOD);
}

//fill the f_final
void convolution(vector<int_t>& F, vector<int_t>& G, long_t f_max, long_t g_max){
//    cout<<"Conv:"<<endl;
//    print_v(F, f_max);
//    print_v(G, g_max);
    
    long_t zero = 0;
    vector<int_t> R(f_max+g_max + 1);
    //n2<=n1;
    for (long_t x = 0; x <= f_max + g_max; ++x){
        for (long_t y = max(g_max, x) - g_max; y<=min(x, f_max); ++y) {
            mulmodsum(R[x],F[y],G[x-y]);
        }
    }
    for (long_t i = 0; i <= f_max+g_max; ++i) F[i] = R[i];
//    print_v(F, f_max + g_max);
}

void conv_power(vector<int_t>& p, int k){
    
    long_t p_max = p.size()-1;
    
    vector<int> bits;
    while(k > 0){
        bits.push_back(k&1);
        k>>=1;
    }
    
    
    bool first = true;
    for(int r = bits.size()-1; r >= 0; --r){
        convolution(f, f, f_max, f_max);
        f_max*=2;
        if (bits[r]==1){
            if (first){
                for (int_t i = 0; i <= p_max; ++i) f[i] = p[i];
                first = false;
            }
            else{
                convolution(f, p, f_max, p_max);
            }
            f_max += p_max;
        }
    }
//    print_v(f, f_max);
}



int main(){
    int_t n;
    int_t m;
    int_t k;
    cin >> n >> m >> k;
    
    f.resize((m-1)*k+1);
    f[0] = 1;
    f_max = 0;
    
    vector<int_t> v(n);
    for(int i = 0; i < n; i++){
       cin >> v[i];
       (v[i])--;
    }
    vector<int_t> p(m);
    for(int_t p_i = 0; p_i < m; p_i++){
       cin >> p[p_i];
    }
    
    
    vector<int_t> res(n);
    vector<int_t> val(n);
    for (int_t i = 0 ; i < n; ++i) val[i] = i;
    
    conv_power(p, k);
    
    //cout<<(3*modinv(9))%MOD;
    //cout<<endl;
    //print_v(f, f_max);
    
    
    
    for (int_t i = 0; i <= (m-1)*k; ++i){
        if (f[i]!=0){
            //sum up the probs
            for (int j=0; j < n; ++j){
                res[val[j]] = (res[val[j]] + f[i])%MOD;
            }
            //update the vector
            for (int j = 0; j < n; ++j){
                val[j] = v[val[j]];
            }
        }
    }
    //adjust the prob
    int_t pn = modinv(n);
    for (int j = 0; j < n; ++j){
        mulmod(res[j], pn);
        cout<<res[j]<<endl;
    }
    
    return 0;
}
