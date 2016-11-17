#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;


struct rect{
        int x1, y1, x2, y2;
};

struct point{
        int x, y;
};

bool isin(rect r, point p){
    return ( (r.x1<p.x)&&(p.x<r.x2)&&(r.y1<p.y)&&(p.y<r.y2) );
}

//BASIC BRUTEFORCE
int main() {
    unordered_map<int, rect> rects;
    
    int n , q;
    cin >> n>>q;
    
    point p[n];
    
    for (int i; i < n; ++i){
        cin >> p[i].x >> p[i].y;
    }
    
    for (int i = 0; i < q; ++i){
        string query_s;
        cin>>query_s;
        if (query_s=="add"){
            rect r;
            cin>>r.x1>>r.y1>>r.x2>>r.y2;
            rects[i+1] = r;
        }
        else if (query_s =="delete"){
            int i;
            cin>>i;
            rects.erase(i);
        }
        else{
            int ia, ib;
            cin >> ia >>ib;
            ia--; ib--;
            bool res = true;
            for (unordered_map<int, rect>::iterator it = rects.begin(); it!= rects.end(); ++it){
                bool ina = isin(it->second, p[ia]);
                bool inb = isin(it->second, p[ib]);
                if ((ina && !inb)||(!ina && inb)){
                    res = false;
                    break;
                }
            }
            if (res) cout<<"YES"<<endl;
            else cout<<"NO"<<endl;
        }
    }
    return 0;
}
