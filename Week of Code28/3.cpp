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
#include <cassert>
#include <algorithm>
#include <unordered_map>

using namespace std;

const long long MOD = 1000000007;

int main(){
    int n;
    cin >> n;
    string number;
    cin >> number;
    // your code goes here
    unsigned long long res;
    res = 0;
    
    //D stores number of substring ending in the XY
    unsigned long long D[100] = {0};
    unsigned long long D_old[100] = {0};
    
    
    //H stores number of characters with value X
    unsigned long long H[10] = {0};
    unsigned long long H_old[10] = {0};
    
    
    for(int i = 0; i < n; ++i){
        /*calculate res based on previous values*/
        
        //retreive digit
        int digit = number[i] - '0';
        assert(digit>=0);
        assert(digit<=9);
        
        //calculate 1 ending here
        if ((digit==8)||(digit==0)) {++res;
                                 //    cout<<digit<<endl;
                                    }
        
        //calculte 2 ending here
        for (int j = 0; j < 10; ++j){
            if ((10*j + digit)%8 == 0) {res+=H[j];
                                  //      cout<<10*j + digit<<" "<<H[j]<<endl;
                                       }
        }
        
        //calculate 3 and more ending here
        for (int j = 0; j < 100; ++j){
            if ((10*j + digit)%8 == 0) {res+=D[j];
                                   //      cout<<10*j + digit<<" "<<D[j]<<endl;
                                       }
        }
        
        res%=MOD;
        
        /*update the values*/
        
        //save old values
        //for (int j = 0; j < 100; ++j) D_old[j] = D[j];
        //for (int j = 0; j < 10; ++j) H_old[j] = H[j];
        copy(D, D+100, D_old);
        copy(H, H+10, H_old);
        //update D
        ////count triples
        for (int j = 0; j < 100; ++j){
            D[10*(j%10) + digit] += D_old[j];
        }
        
        ////count pairs
        for (int j = 0; j < 10; ++j){
            D[10*j + digit]+=H_old[j];
        }
        
        ////module
        for (int j = 0; j < 100; ++j){
            D[j]%=MOD;
//            cout<<D[j]<<" ";
        }
        
//        cout<<endl;
        
        //update H
        H[digit]++;
        
//        cout<<endl;
//        cout<<endl;
    }
    
    cout<<res%MOD;
    // end of code
    return 0;
}
