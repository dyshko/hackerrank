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

unordered_map<string, int> dp;

//partition and gluing first and last (if any)
vector<string> partition(const string& s, char x){
        vector<string> strs;
        int n = s.length();
        string tmp = "";
        for (int i = 0; i < n; ++i){
            if (s[i]!=x) tmp+=s[i];
            if ((s[i]==x)&&(i>0)&&(s[i-1]!=x)){
                strs.push_back(tmp);
                tmp = "";
            }
        }
        if (tmp!=""){
            if ((s[0]!=x)&&(strs.size()>0))
                strs[0] = tmp + strs[0];
            else 
                strs.push_back(tmp);
        }
        return strs;
}

inline char smallest(const string& s){
    char res = 'z';
    for (int i = 0; i < s.length(); ++i) if (res > s[i]) res = s[i];
    return res;
}

int eliminate(const string& s){
    
    int n = s.length();
    if (n<=1) return 0;
    
    if (dp.find(s)!=dp.end()) return dp[s];
    //cout<<"Test:"<<s<<endl;
    char x = smallest(s);
    vector<string> strs = partition(s, x);
    int k = strs.size();
    
    //check if any strings in partition
    if (k == 0) return 0;
    
    int res = 1000000;
    if ((s[0]==x)&&(s[n-1]!=x)){
        for (int i = 1; i < k; ++i){
            string tmp = "";
            for (int j = i; j < k; ++j) tmp+=strs[j];
            for (int j = 0; j < i; ++j) tmp+=strs[j];
            int val = eliminate(tmp) + k -1;
            res = min(res, val);
        }
        if (k == 1){
            return eliminate(strs[0]);
        }
    }else{
        for (int i = 0; i < k; ++i){
            string tmp = "";
            for (int j = i; j < k; ++j) tmp+=strs[j];
            for (int j = 0; j < i; ++j) tmp+=strs[j];
            int val = eliminate(tmp) + k;
            res = min(res, val);
        }
    }
    
    //if (res>0) cout<<s<<" "<<res<<endl;
    
    dp[s] = res;
    
    return res;
}

int main(){
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        string s;
        cin >> s;
        cout<<eliminate(s)<<endl;
    }
    return 0;
}
