#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <queue>
using namespace std;

void BFS(unordered_map<int, vector<int>> &G, int u, long av[], int typ, long x, int comp[]){
    
    if (comp[u]==1){
        if (typ==1) av[u] = x;
        else av[u] = min(av[u],x);
        if (G.find(u)!=G.end()){
            for (vector<int>::iterator it = G[u].begin(); it!=G[u].end(); it++){
                    if (typ==1) av[*it] = x;
                    else av[*it] = min(av[*it],x);
                }
            }
        return;
    }
    
    queue<int> Q;
    Q.push(u);
    comp[u]=1;
    unordered_map<int,char> visited;
    
    if (!Q.empty()){
        Q.pop();
        if (G.find(u)!=G.end()){
            for (vector<int>::iterator it = G[u].begin(); it!=G[u].end(); it++){
                if (visited.find(*it) == visited.end()){
                    visited[*it]=1;
                    Q.push(*it);
                }
            }
        }
        if (typ==1) av[u] = x;
        else av[u] = min(av[u],x);
    }
    
    while (!Q.empty()){
        int v0 = Q.front();
        Q.pop();
        if (G.find(v0)!=G.end()){
            for (vector<int>::iterator it = G[v0].begin(); it!=G[v0].end(); it++){
                if (visited.find(*it) == visited.end()){
                    visited[*it]=1;
                    Q.push(*it);
                }
            }
        }
        G[u].push_back(v0);
        if (typ==1) av[v0] = x;
        else av[v0] = min(av[v0],x);
    }
}

int main() {
   int n, m , Q;
   cin>>n>>m>>Q;
   unordered_map<int, vector<int>> G;
   long av[n+1] = {0};
   int comp[n+1] = {0};
   for (int i = 0; i < m; ++i){
       int u, v;
       cin>>u>>v;
       if (G.find(u)==G.end()){
           G[u] = vector<int>(0);
       }
       G[u].push_back(v);
   }
   
   for (int q_it= 0; q_it < Q; ++q_it){
       int typ, u;
       long x;
       cin>>typ>>u;
       if (typ == 1){
           cin>>x;
           BFS(G, u, av, 1, x, comp);
       }
       else if (typ == 2){
           cin>>x;
           BFS(G, u, av, 2, x, comp);
       }
       else{
           cout<<av[u]<<endl;
       }
   }
   return 0;
}

