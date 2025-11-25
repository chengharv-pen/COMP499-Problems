#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;

const int DEBUG_LEVEL = 0;
vector<int> dfs_order_rev;

void dfs_visit(int v, const vector<vector<int>> & adj, vector<int> &marked, int mark) {
    for(int neighbor : adj[v]) {
        if(marked[neighbor] == -1) {
            marked[neighbor] = mark;
            dfs_visit(neighbor, adj, marked, mark);
        }
    }
    dfs_order_rev.push_back(v); // order of vertices by increasing finishing time
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
    vector<int> marked(2*n, -1);
    dfs_order_rev.clear();
    for(int i = 0; i < 2*n; i++) {
        if(marked[i] == -1) {
            marked[i] = 1;
            dfs_visit(i, adj, marked, 1);
        }
    }
    //cout << dfs_order_rev.size() << endl;


    // copy the order of vertices
    vector<int> dfs_order_rev_copy = dfs_order_rev;
    dfs_order_rev.clear();
    marked.assign(2*n, -1);
    int comp_no = 0;
    /* Run the second DFS */
    for(auto it = dfs_order_rev_copy.rbegin(); it != dfs_order_rev_copy.rend(); it++) {
        int v = *it;
        if(marked[v] == -1) {
            marked[v] = comp_no;
            dfs_visit(v, adj_rev, marked, comp_no);
            comp_no++;
        }
    }

    /* Compute assignment */
    vector<bool> assignment(n, false);
    bool is_sat = true;
    for(int i = 0; i < n; i++) {
        int comp_i = marked[i];
        int comp_neg_i = marked[negate_literal(i,n)];
        if(comp_i == comp_neg_i) {
            is_sat = false;
            //cout << i << comp_i << endl;
            break;
        } else if (comp_i > comp_neg_i) {
            assignment[i] = true;
        } else {
            assignment[i] = false;
        }
    }

    if(!is_sat) {
        cout << "bad luck" << endl;
    } else {
        for(int i = 1; i < n; i++) {
            cout << i << (assignment[i]?("w"):("h"));
            if(i < n-1) {
                cout << " ";
            } else {
                cout << endl;
            }
        }
    }

    return 0;
}