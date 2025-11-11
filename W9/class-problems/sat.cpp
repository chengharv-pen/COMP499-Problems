// kattis problem: https://open.kattis.com/problems/satisfiability

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

#define debug_level 0

void print_clause(int clause_num, const vector<vector<int>> &clauses) {
    cout << "Clause " << clause_num << ":";
    for(int var : clauses[clause_num])
        cout << " " << var;
    cout << endl;
}

void print_assignment(int n, int tau) {
    cout << "assignment corresponding to " << tau << endl;
    for(int i = 0; i < n; i++) {
        cout << "\tx_" << (i+1) << " = ";
        if(tau & (1 << i)) {
            cout << "true";
        } else {
            cout << "false";
        }
        cout << endl;
    }
}

int main() {
    string str;
    getline(cin, str);
    stringstream ss(str);
    int t;
    ss >> t;

    for(int zzz = 0; zzz < t; zzz++) {
        getline(cin,str);
        ss.clear();
        ss.str(str);
        int n,m;
        ss >> n >> m;

        vector<vector<int>> clauses(m,vector<int>());
        for(int i = 0; i < m; i++) {
            getline(cin, str);
            ss.clear();
            ss.str(str);
            string tok;
            while(ss >> tok) {
                if(tok[0] == 'v') continue;
                int j;
                int sign = 1;
                if(tok[0] == '~') {
                    j = 2;
                    sign = -1;
                } else
                    j = 1;
                int var = 0;
                for(; j<tok.length(); j++) {
                    var *= 10;
                    var += (int) (tok[j]-'0');
                }
                clauses[i].push_back(sign*var);
            }
            if(debug_level >= 2) print_clause(i, clauses);

        }
        bool found = false; // have we found satisfying assignment?
        // search for satisfying assignment
        for(int tau = 0; tau < (1<<n); tau++) {
            if(debug_level >= 2) print_assignment(n, tau);
            bool sat = true; // does tau satisfy all the clauses so far?
            for(int i = 0; i < m; i++) {
                // check if tau satisfies clause i
                bool cl_sat = false;
                for(int k = 0; k < clauses[i].size(); k++) {
                    int lit = clauses[i][k];

                    // needs to be done!!!
                    // if literal appears negatively, it is satisfied when corresponding variable is set to false in tau
                    // if literal appears positively, it is satisfied when corresponding variable is set to true in tau
                    // variable i corresponds to position (i-1) in tau
                }
                if(!cl_sat) { // this tau does not satisfy all clauses
                    sat = false;
                    break;
                }
            }
            if(sat) { // found satisfying assignment
                found = true;
                break;

            }
        }
        if(found) {
            cout << "satisfiable" << endl;
        } else {
            cout << "unsatisfiable" << endl;
        }
    }
    return 0;
}