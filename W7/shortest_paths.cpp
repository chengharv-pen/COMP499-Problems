#include <iostream>
#include <utility>
#include <queue>


using namespace std;

# define INF 0x3f3f3f3f

/* this already exists for the pair type, but I want to show how is done in case we have other types that do not have a predefined operator

 We need greater because in STL C++ the priority queue uses a max heap so to get a min heap we revert the operator
 */
struct mygreater {
        const bool operator()(const pair<int, int>& a, const pair<int, int>& b) const {
            return a.second>b.second;
        }
    };

int main(){

    int n = 0, m = 0;
    cin>>n>>m;

    // adjacency list
    vector<vector<pair<int, int> > >adj(n);
    vector<int> distance(n, INF);
    vector<int> parent(n, -1);
    vector<bool> processed(n,false);

    for(int i=0;i<m;++i){
        int j=0, k=0, w=0;
        cin>>j>>k>>w;

        adj[j-1].push_back(pair<int, int>(k-1, w));
        adj[k-1].push_back(pair<int, int>(j-1, w));

    }


    // run Dijkstra
    priority_queue< pair<int, int>, vector <pair<int, int> > > pq;
    distance[0] = 0;
    pq.push(pair<int, int>(0, 0));
    while(!pq.empty()){
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();
        if(processed[u])
            continue;
        processed[u] = true;

        for(int i=0;i<adj[u].size();++i){
            if(processed[adj[u][i].first]==false && d+adj[u][i].second<distance[adj[u][i].first]){
                distance[adj[u][i].first] = d+adj[u][i].second;
                pq.push(adj[u][i]);
            }
        }
    }// while

    cout<<distance[0];
    for(int i=1;i<n;++i){
        cout<<" "<<distance[i];
    }

    return 0;
}