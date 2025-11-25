#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define ll long long

pair<ll,ll> P;

pair<ll,ll> operator-(const pair<ll,ll> &p1, const pair<ll,ll> &p2) {
    return {p1.first - p2.first, p1.second - p2.second};
}

ll det(const pair<ll,ll> &p1, const pair<ll,ll> &p2) {
    return p1.first * p2.second - p1.second*p2.first;
}

ll norm_sq(const pair<ll,ll> &p) {
    return p.first*p.first + p.second*p.second;
}

bool custom_comp(const pair<ll, ll> &p1, const pair<ll,ll> & p2) {
    ll cp = det(p1-P, p2-P);
    if(cp == 0) {
        return norm_sq(p1-P) < norm_sq(p2-P);
    }
    return cp > 0;
}

void print_ch(const vector<pair<ll,ll>> & pts) {
    cout << pts.size() << endl;
    for(int i = 0; i < pts.size(); i++) {
        cout << pts[i].first << " " << pts[i].second << endl;
    }
}

int main() {
    int n;
    while((cin >>n) && n) {
        vector<pair<ll,ll>> pts;
        for(int i = 0; i <n; i++) {
            ll x, y;
            cin >> x >> y;
            if(i == 0 || y < P.second || (y == P.second && x < P.first)) {
                P = make_pair(x,y);
            }
            pts.push_back({x,y});
        }
        // eliminate duplicates
        sort(pts.begin(), pts.end());
        auto ptr = unique(pts.begin(), pts.end());
        pts.erase(ptr,pts.end());
        n = pts.size();

        if( n <= 2) {
            print_ch(pts);
        } else {
            sort(pts.begin(), pts.end(), custom_comp);
            vector<pair<ll,ll>> res;
            res.push_back(pts[0]);
            res.push_back(pts[1]);
            for(int i = 2; i < pts.size(); i++) {
                // while res[end-2], res[end-1],pts[i] makes right turn, remove last vertex from res
            }
            print_ch(res);
        }

    }
    return 0;
}