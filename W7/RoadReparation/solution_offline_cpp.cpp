
/* Based largely on
 https://www.geeksforgeeks.org/prims-algorithm-using-priority_queue-stl/
 Fixed some bugs
 */

#include <utility>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;
# define INF 0x3f3f3f3f
 
 
// This class represents a directed graph using
// adjacency list representation
class Graph
{
public:
    int m_n;    // No. of vertices
 
    vector<vector<pair<int, int> > > m_adj;
    
 
public:
    Graph(int n);  // Constructor
    Graph();
    void resize(int n);
 
    // function to add an edge to graph
    void addEdge(int u, int v, int w);
 
    // Print MST using Prim's algorithm
    void primMST();

    // output of te Prim's algorithm
    vector<int> m_key, m_parent;

};

Graph::Graph(){

    m_n = 0;
}

void Graph::resize(int n){

    m_n = n;
    m_adj.resize(n);
}


Graph::Graph(int n)
{
   resize(n);
}
 
void Graph::addEdge(int u, int v, int w)
{
    m_adj[u].push_back(make_pair(v, w));
    m_adj[v].push_back(make_pair(u, w));
}
 



// Prints shortest paths from src to all other vertices
void Graph::primMST()
{

    priority_queue< pair<int, int>, vector <pair<int, int> > , mygreater > pq;

    int src = 0; // Taking vertex 0 as source
 
    // Create a vector for keys and initialize all
    // keys as infinite (INF)
    vector<int> key(m_n, INF);
 
    // To store parent array which in turn store MST
    vector<int> parent(m_n, -1);
 
    // To keep track of vertices included in MST
    vector<bool> processed(m_n, false);
 
    // Insert source itself in priority queue and initialize
    // its key as 0.
    pq.push(make_pair(src, 0));
    key[src] = 0;

    /* Looping till priority queue becomes empty */
    while (!pq.empty())
    {
        // The first vertex in pair is the minimum key
        // vertex, extract it from priority queue.
        // vertex label is stored in second of pair (it
        // has to be done this way to keep the vertices
        // sorted key (key must be first item
        // in pair)
        int u = pq.top().first;
        pq.pop();
         
          //Different key values for same vertex may exist in the priority queue.
          //The one with the least key value is always processed first.
          //Therefore, ignore the rest.
          if(processed[u]){
            continue;
        }
       
        processed[u] = true;  // Include vertex in MST
 
        
        for(int i=0;i<m_adj[u].size();++i){
            int v = m_adj[u][i].first;
            int w = m_adj[u][i].second;
            
            if(processed[v]==false && key[v] > w)
            {
                // Updating key of v
                key[v] = w;
                pq.push(make_pair(v, key[v]));
                parent[v] = u;
            }
        }
        
    }

    m_key = key;
    m_parent = parent;


}

void readinput(Graph& g){
    int n = 0;
    cin>>n;
    int m = 0;
    cin>>m;

    g.resize(n);

    for(int i=0;i<m;++i) {
        int a = 0, b = 0, w = 0;
        cin >> a >> b >> w;
        g.addEdge(a-1, b-1, w);

    }
}




void unittesting(){

    // create the graph given in above figure
    int N = 9;

    Graph g(N);

    //  making above shown graph
    g.addEdge(0, 1, 2);
    g.addEdge(0, 7, 8);
    g.addEdge(1, 2, 8);
    g.addEdge(1, 7, 11);
    g.addEdge(2, 3, 7);
    g.addEdge(2, 8, 2);
    g.addEdge(2, 5, 4);
    g.addEdge(3, 4, 9);
    g.addEdge(3, 5, 14);
    g.addEdge(4, 5, 10);
    g.addEdge(5, 6, 2);
    g.addEdge(6, 7, 1);
    g.addEdge(6, 8, 6);
    g.addEdge(7, 8, 7);


    g.primMST();
    
#if 1 // unit testing
    // Print edges of MST using parent array
    int sum = 0;
    for (int i = 1; i < g.m_n; ++i) {
        sum+=g.m_key[i];
        printf("%d - %d\n", g.m_parent[i], i);
    }
    std::cout<<sum<<std::endl;
#endif


}



// Driver program to test methods of graph class
int main()
{
   // unittesting();
 //return 0;

    Graph g;
    readinput(g);

    g.primMST();

    int sum = 0;
    for (int i = 0; i < g.m_n; ++i) {
        sum+=g.m_key[i];
        //printf("%d - %d\n", g.parent[i], i);
    }
    std::cout<<sum<<std::endl;

    return 0;
}
