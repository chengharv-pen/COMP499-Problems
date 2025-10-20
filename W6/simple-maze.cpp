#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int main(){


    // STEP 1 --> READING INPUT
    int n=0, m=0;
    cin>>n>>m;

    vector<char> V(n*m), O(n*m);
    vector<int> C(n*m), D(n*m), P(n*m);
    int a = 0, b = 0;
    for(int i=0;i<n;++i){
        string s;
        cin>>s;

        for(int j=0;j<s.length();++j){
            V[i*m+j] = s[j];
            C[i*m+j] = 0;// 0 white
            D[i*m+j] = -1;// -1 means infinity
            P[i*m+j]= -1;// -1 means NIL

            if(s[j]=='A')
                a = i*m+j;
            if(s[j]=='B')
                b = i*m+j;

        }
    }

    // STEP 2
    queue<int> q;
    q.push(a);
    C[a] = 1;// 1 - grey
    D[a] = 0;

    // 4 neihgbours
    int directions [4] = {1, -1, m, -m};
    string dirc = "RLDU";

    bool success = false;
    while(!q.empty() && !success){
        int e = q.front();
        q.pop();

        int r = e / m;
        int c = e % m;
        for(int j=0;j<4;++j){

            if(j==0 && c==m-1 || j==1 && c== 0 || j == 2 && r==n-1 || j==3 && r==0)
                continue;


            int nei = e + directions[j];

            if(V[nei]=='.' || V[nei]=='B'){
                if(C[nei]==0){
                    q.push(nei);
                    C[nei] = 1;
                    D[nei] = 1 + D[e];
                    P[nei] = e;
                    O[nei] = dirc[j];
                }
            }

            if(V[nei]=='B'){
                success = true;
                break;
            }

        }// for

    }// while

    if(success == true){
        cout<<"YES"<<endl;
        cout<<D[b]<<endl;
        string os;
        while(b!=a){
            os.push_back(O[b]);
            b = P[b];
        }
        reverse(os.begin(), os.end());
        cout<<os;
    } else {
        cout<<"NO";
    }


    return 0;
}