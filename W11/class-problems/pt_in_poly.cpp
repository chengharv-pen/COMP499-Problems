#include <iostream>
#include <vector>
using namespace std;

#define ll long long

pair<ll,ll> operator-(const pair<ll,ll> &p1, const pair<ll,ll> &p2) {
    return {p1.first - p2.first, p1.second - p2.second};
}

ll det(const pair<ll,ll> &p1, const pair<ll,ll> &p2) {
    return p1.first * p2.second - p1.second*p2.first;
}

ll norm_sq(const pair<ll,ll> &p) {
    return p.first*p.first + p.second*p.second;
}

int main() {
    int n,m;
    while((cin >> n) && n) {
        vector<pair<ll,ll>> poly;
        for(int i = 0; i < n; i++) {
            ll x,y;
            cin >> x >> y;
            poly.push_back({x,y});
        }
        poly.push_back(poly[0]);

        cin >> m;
        for(int z = 0; z < m; z++) {
            ll x,y;
            cin >> x >> y;
            int count = 0;
            bool on = false;
            for(int i = 0; i < n; i++) {
                pair<ll,ll> t,b;
                if((poly[i].second > poly[i+1].second) ||
                    (poly[i].second == poly[i+1].second && poly[i].first < poly[i+1].first)) {
                    t = poly[i];
                    b = poly[i+1];
                } else {
                    t = poly[i+1];
                    b = poly[i];
                }
                if(y < b.second || y > t.second) continue;
                if(b.second == t.second) {
                    if(x >= t.first && x <= b.first) {
                        on = true;
                        break;
                    }
                } else if (y == t.second) {
                    if(x == t.first) {
                        on = true;
                        break;
                    }
                } else if (y == b.second) {
                    if(x == b.first) {
                        on = true;
                        break;
                    } else if (x < b.first) {
                        count++;
                    }
                } else { // general case
                    pair<ll,ll> p({x,y});
                    ll cp = det(b-t,p-t);
                    if(cp == 0) {
                        on = true;
                        break;
                    } else if (cp < 0) {
                        count++;
                    }
                }
            }
            if(on) {
                cout << "on" << endl;
            } else if (count%2 == 1) {
                cout << "in" << endl;
            } else {
                cout << "out" << endl;
            }
        }
    }
    return 0;
}