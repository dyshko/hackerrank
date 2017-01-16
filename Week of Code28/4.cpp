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

typedef unsigned long long long_t;

//add from c2 to c1
inline void add(vector<int>* c1_pt, vector<int>* c2_pt, vector<int>* get_clique[]){
    if (c1_pt == c2_pt) return;
    c1_pt->insert(c1_pt->end(), c2_pt->begin(), c2_pt->end());
    for (auto& el: *c2_pt){
        get_clique[el] = c1_pt;
    }
    c2_pt->clear();
}

long_t foo(long_t x){
    long_t res;
    res = (x*(x+1)*(2*x+1))/6;
    res -= (x*(x+1))/2;
    return res;
}

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        int m;
        cin >> n >> m;
        
        //clique with the corresponing ingex;
        vector<int> clique[n];
        
        for (int i = 0; i < n; ++i){
            clique[i].push_back(i);
        }
        
        //get the reference to the clique
        vector<int>* get_clique[n];
            
        for (int i = 0; i < n; ++i){
                get_clique[i] = &clique[i];
        }
        
        long_t res = 0;
        long_t total = 0;
        
        
        
        for(int a1 = 0; a1 < m; a1++){
            int x;
            int y;
            cin >> x >> y;
            --x;
            --y;
            
            //combine two cliques
            vector<int>* c1_pt = get_clique[x];
            vector<int>* c2_pt = get_clique[y];
            
            if (c1_pt!=c2_pt){
                long_t size1 = c1_pt->size();
                long_t size2 = c2_pt->size();
            
                if (size2 < size1){
                    add(c1_pt, c2_pt, get_clique);
                }
                else{
                    add(c2_pt, c1_pt, get_clique);
                }
            }
        }
        vector<int> sizes;
        for (int i = 0; i < n; ++i){
            if (clique[i].size() > 1){
                sizes.push_back(clique[i].size());
            }
        }
        sort(sizes.begin(), sizes.end(), greater<int>());
        
        int sum = 0;
        for (auto s: sizes){
            for (int i = 0; i < s-1; ++i){
                total += 2*(i+1);
                res+=total;
                //cout<<s<<" "<<total<<" "<<res<<endl;
            }
            sum+=s-1;
            
            
        }
        res += (m - sum)*total;
        //
        
        
        
        cout<<res<<endl;
    }
    return 0;
}
