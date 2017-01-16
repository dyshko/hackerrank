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

int main(){
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        long x;
        cin >> x;
        
        long t;
        t = x;
        
        long mask = 0;
        
        while (t>0){
            mask<<=1;
            mask+=1; 
            t>>=1;
        }
        // your code goes here
        cout<<(x^mask)<<endl;
        
    }
    return 0;
}
