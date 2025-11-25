#include <iostream>
using namespace std;

#define ll long long

pair<ll,ll> operator-(const pair<ll,ll> &p1, const pair<ll,ll> &p2) {
    return {p1.first - p2.first, p1.second - p2.second};
}

ll det(const pair<ll,ll> &p1, const pair<ll,ll> &p2) {
    return p1.first * p2.second - p1.second*p2.first;
}

int main() {
    int t;
    cin >> t;
    for(int zzz = 0; zzz < t; zzz++) {
        ll x1,y1,x2,y2,x3,y3;
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
        pair<ll, ll> p1={x1,y1};
        pair<ll, ll> p2={x2,y2};
        pair<ll, ll> p3={x3,y3};
        ll cp = det(p2-p1, p3-p1);
        if(cp == 0) {
            cout << "TOUCH" << endl;
        } else if (cp > 0) {
            cout << "LEFT" << endl;
        } else {
            cout << "RIGHT" << endl;
        }
    }

    return 0;
}