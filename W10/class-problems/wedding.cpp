#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;

const int DEBUG_LEVEL = 3;
stack<int> dfs_order;

void dfs_visit(int v, const vector<vector<int>> & adj, vector<int> &marked, int mark) {
    for(int neighbor : adj[v]) {
        if(marked[neighbor] == -1) {
            marked[neighbor] = mark;
            dfs_visit(neighbor, adj, marked, mark);
        }
    }
    dfs_order.push(v);
}

int negate_literal(int lit, int n) {
    return (lit + n) % (2*n);
}

/*
    Process input token of the form [pair_number][h/w]
    Positive literals are indicated by numbers 0, 1, ..., n-1
    Negative literals are indicated by numbers n, n+1, ..., 2n-1
    For example, 8h returns 8 while 8w returns 18 when n = 10
*/
int get_literal(string name, int n) {
    int idx = 0;
    int len = name.size();
    for(int i = 0; i < len-1; i++) {
        idx *= 10;
        idx += (int)(name[i]-'0');
    }
    if(name[len-1] == 'h') {
        return idx;
    } else {
        return idx + n;
    }
}

void print_adj(const vector<vector<int>> & adj) {
    int N = adj.size();
    for(int i = 0; i < N; i++) {
        cout << i << ":";
        for(int j : adj[i]) {
            cout << " " << j;
        }
        cout << endl;
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(2*n, vector<int>());
    vector<vector<int>> adj_rev(2*n, vector<int>());
    for(int i = 0; i < m; i++) {
        string tok1, tok2;
        cin >> tok1 >> tok2;
        int lit1, lit2;
        lit1 = get_literal(tok1, n);
        lit2 = get_literal(tok2, n);
        if(DEBUG_LEVEL >= 2) {
            cout << "pair " << i << ": " << lit1 << " " << lit2 << endl;
        }
        /* Construct implication graph */
        int neg_lit1 = negate_literal(lit1,n);
        int neg_lit2 = negate_literal(lit2,n);
        adj[lit1].push_back(neg_lit2);
        adj[lit2].push_back(neg_lit1);
        /* Construct transpose/reverse */
        adj_rev[neg_lit2].push_back(lit1);
        adj_rev[neg_lit1].push_back(lit2);
    }
    /* encode clause (x_0) */
    adj[negate_literal(0,n)].push_back(0);
    adj_rev[0].push_back(negate_literal(0,n));

    if(DEBUG_LEVEL >= 3) {
        cout << "Implication Graph:" << endl;
        print_adj(adj);
        cout << "Reverse of Implication Graph:" << endl;
        print_adj(adj_rev);

    }

    /* Run the first DFS */

    /* Run the second DFS */

    /* Compute assignment */
    return 0;
}