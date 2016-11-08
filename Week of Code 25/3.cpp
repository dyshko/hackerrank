#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int num(int a, int b, int d){
    int res = d/b;
    d%=b;
    //now d is smaller than b; and 1 more steps are ok
    if (d>0){
        if (res>0){
            res++;
        }
        else{//d<b and res=0
            if (d==a){
                res++;
            }
            else{
                res+=2;
            }
        }
    }
    return res;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int Q;
    cin>>Q;
    for (int q = 0; q< Q; ++q){
        int a,b,d;
        cin>>a>>b>>d;
        cout<<num(a,b,d)<<endl;
    }
    return 0;
}
