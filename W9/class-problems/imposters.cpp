// kattis problem: https://open.kattis.com/problems/investigatingimposters

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stack>
#include <map>
using namespace std;

int main() {
    int n,k;
    cin >> n >> k;
    vector<vector<int>> adj(n, vector<int>());

    for(int i = 0; i < n; i++) {
        int s;
        //vilager i
        cin >> s; // size of the list of villager i
        for(int j = 0; j < s; j++) {
            int u;
            cin >> u;
            u--;
            adj[u].push_back(i); // add edge (u,i) in G^R
        }
    }

    // run BFS from every villager
    for(int v = 0; v < n; v++) {
        // run BFS from v
        vector<bool> visited(n, false);
        queue<int> q;
        //initialize BFS: q contains the current wave frontier
        q.push(v);
        visited[v] = true;
        while(!q.empty()) {
            int cur = q.front();
            q.pop();
            for(int neighbor : adj[cur]) {
                if(!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        // compute how many were visited
        int count = 0;
        for(int i = 0; i < n; i++) {
            if(visited[i])
                count++;
        }
        if(count > k)
            cout << 1 << endl;
        else
            cout << 0 << endl;
    }
    return 0;
}