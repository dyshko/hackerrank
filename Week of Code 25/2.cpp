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

int common(string s, string t){
    int i = 0;
    while ((i < s.length()) && (i<t.length()) && s[i] == t[i]){
        i++;
    }
    return i;
}

int main(){
    string s;
    cin >> s;
    string t;
    cin >> t;
    int k;
    cin >> k;
    int x = common(s,t);
    int val =  k + 2*x - s.length() - t.length();
    if (val < 0){
        cout<<"No";
    }
    else{
        if (val <= 2*x){
            if (val%2==0){
                cout<<"Yes";
            }
            else{
               cout<<"No"; 
            }
        }
        else{
            cout<<"Yes";
        }
    }
    return 0;
}
