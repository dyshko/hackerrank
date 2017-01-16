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


typedef unsigned long int long_t;

static int K;
static int N;
static int W;
static int B;

inline int at(long_t s, int i){
    return (s&(1<<(i)))>>i;
}

inline long_t remove(long_t s, int i){
    long_t tmp = s&((1<<i) - 1);
    s>>=(i+1);
    s<<=i;
    return s^tmp;
}

inline int get_whites(long_t s, int n){
    int res = 0;
    for (int i = 0; i < n; ++i){
        //cout<<" "<<(s&(1<<i));
        if (!(s&(1<<i))) {++res;}
    }
    return res;
}

inline long_t to1(long_t s, int n){
    return s+(1<<n);
}

typedef map<long_t, double> memo_t;

static memo_t dp;

//scheme - balls
//n      - number of balls
inline double foo(long_t s, int n){
    
    long_t key = to1(s,n);
    if (dp.find(key)!=dp.end()){
        return dp[key];
    }
    
    int w = get_whites(s,n);
    int b = n - w;
    
    if (n == N - K) return 0;
    
    if (w==0) return 0;
    if (b==0) return n-N+K;
    
    double res = 0;
    // here n > N - K and we may delete one element
    for (int i = 0; i < n/2; ++i){
        //do stuff
        int L = at(s,i);
        int R = at(s,n-i-1);
        double left = foo(remove(s, i), n-1);
        double right = foo(remove(s, n-i-1), n-1);
        res+=(2/(double)n)*max(left + (1 - L), right + (1 - R));
    }
    //not forget about the middle element
    if (n%2==1){
        //do stuff
        int C = at(s,n/2);
        double center = foo(remove(s, n/2), n-1);
        res+= (1/(double)n)*(center+(1-C));
    }
    dp[key] = res;
    return res;
}

int main(){
    cout.precision(17);
    cin >> N >> K;
    string balls;
    cin >> balls;
    long_t s;
    for(int i = 0; i < N; ++i){
        s<<=1;
        if (balls[i]=='B') {s|=1;++B;}
        else ++W;
    }
    cout<<foo(s, N);
    //cout<<get_whites(0,10);
    //cout<<endl<<remove(8,3);
    // your code goes here
    return 0;
}
