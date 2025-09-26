#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct Episode {
    int s;
    int f;
    int e;
    int idx; // original index

    Episode(int s_, int f_, int e_, int idx_): s(s_), f(f_), e(e_), idx(idx_) {}

    bool operator<(const Episode &other) const {
        return f < other.f;
    }
};

int main() {
    int n;

    while ( (cin >>n ) && (n != -1)) {
        vector<Episode> episodes;
        for(int i = 0; i < n; i++) {
            int s, f, e;
            cin >> s >> f >> e;
            episodes.emplace_back(s,f,e,i);
        }
        sort(episodes.begin(), episodes.end());
        vector<int> dp(n, 0);
        vector<int> before(n, -1);
        vector<bool> take_dp(n, false);

        // compute before
        for(int i = 0; i < n; i++) {
            int j = i-1;
            for(; j>=0; j--)
                if(episodes[j].f <= episodes[i].s)
                    break;
            before[i] = j; // -1 indicates nothing is before
        }
        // compute DP
        for(int i = 0; i < n; i++) {
            int take = episodes[i].e;
            if(before[i] >= 0) {
                take += dp[before[i]];
            }
            int skip = (i > 0)?dp[i-1]:0;
            if(take > skip) {
                dp[i] = take;
                take_dp[i] = true;
            } else {
                dp[i] = skip;
                take_dp[i] = false;
            }
        }
        vector<int> sol;
        int id = n-1;
        while(id >= 0) {
            while(!take_dp[id]) {
                id--;
            }
            sol.push_back(episodes[id].idx);
            id = before[id];
        }
        sort(sol.begin(), sol.end());
        cout << dp[n-1] << ":";

        for(int i = 0; i < sol.size(); i++)
            cout << " " << sol[i];

        cout << endl;
    }

    return 0;
}