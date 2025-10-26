import java.util.*;
 
/* Taken mostly from https://www.geeksforgeeks.org/prims-algorithm-using-priority_queue-stl/
 Fixed some bugs
*/



class Pair {
    int first, second;
    public Pair(int first, int second)
    {
        this.first = first;
        this.second = second;
    }
}
 
// This class represents a directed graph using
// adjacency list representation
class Graph {
    int m_n; // No. of vertices
 
    // In a weighted graph, we need to store vertex
    // and weight pair for every edge
    List<List<Pair> > m_adj;
 
    public Graph(int n)
    {
        m_n = n;
        m_adj = new ArrayList<>();
        for (int i = 0; i < m_n; i++) {
            m_adj.add(new ArrayList<>());
        }
    }
 
    // function to add an edge to graph
    void addEdge(int u, int v, int w)
    {
        m_adj.get(u).add(new Pair(v, w));
        m_adj.get(v).add(new Pair(u, w));
    }
 
    // Print MST using Prim's algorithm
    void primMST()
    {
        // Create a priority queue to store vertices that
        // are being primMST. This is weird syntax in Java.
        // Refer below link for details of this syntax
        // https://www.geeksforgeeks.org/implement-min-heap-using-stl/
        PriorityQueue<Pair> pq = new PriorityQueue<>(
            m_n, new Comparator<Pair>() {
                public int compare(Pair a, Pair b)
                {
                    return a.second - b.second;
                }
            });
 
        int src = 0; // Taking vertex 0 as source
 
        // Create a vector for keys and initialize all
        // keys as infinite (INF)
        int INF = Integer.MAX_VALUE;
        int[] key = new int[m_n];
        Arrays.fill(key, INF);
 
        // To store parent array which in turn store MST
        int[] parent = new int[m_n];
        Arrays.fill(parent, -1);
 
        // To keep track of vertices included in MST
        boolean[] inMST = new boolean[m_n];
 
        // Insert source itself in priority queue and
        // initialize its key as 0.
        pq.offer(new Pair(src, 0));
        key[src] = 0;
 
        /* Looping till priority queue becomes empty */
        while (!pq.isEmpty()) {
            // The first vertex in pair is the minimum key
            // vertex, extract it from priority queue.
            // vertex label is stored in second of pair (it
            // has to be done this way to keep the vertices
            // sorted key (key must be first item
            // in pair)
            int u = pq.peek().first;
            pq.poll();
 
            // Different key values for same vertex may
            // exist in the priority queue. The one with the
            // least key value is always processed first.
            // Therefore, ignore the rest.
            if (inMST[u]) {
                continue;
            }
 
            inMST[u] = true; // Include vertex in MST
 
            // 'i' is used to get all adjacent vertices of a
            // vertex
            for (Pair i : m_adj.get(u)) {
                // Get vertex label and weight of current
                // adjacent of u.
                int v = i.first;
                int weight = i.second;
 
                //  If v is not in MST and weight of (u,v)
                //  is smaller
                // than current key of v
                if (!inMST[v] && key[v] > weight) {
                    // Updating key of v
                    key[v] = weight;
                    pq.offer(new Pair(v, key[v]));
                    parent[v] = u;
                }
            }
        }
 
        // Print edges of MST using parent array
        int sum = 0;
        for (int i = 1; i < m_n; i++) {
            System.out.println(parent[i] + " - " + i);
            sum = sum + key[i];
        }
        System.out.println(sum);
    }
}
 
// Driver class
public class solution_offline_java {
    
    
    static void unittesting(){
        // create the graph given in above figure
        int n = 9;
 
        Graph graph = new Graph(n);
 
        //  making above shown graph
        graph.addEdge(0, 1, 2);
        graph.addEdge(0, 7, 8);
        graph.addEdge(1, 2, 8);
        graph.addEdge(1, 7, 11);
        graph.addEdge(2, 3, 7);
        graph.addEdge(2, 8, 2);
        graph.addEdge(2, 5, 4);
        graph.addEdge(3, 4, 9);
        graph.addEdge(3, 5, 14);
        graph.addEdge(4, 5, 10);
        graph.addEdge(5, 6, 2);
        graph.addEdge(6, 7, 1);
        graph.addEdge(6, 8, 6);
        graph.addEdge(7, 8, 7);
 
        graph.primMST();
    }
    
    
    static void fixroads(){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
       
        Graph g = new Graph(n);
        
        Vector<Integer> v = new Vector<>();
        for(int i=0;i<m;i=i+1){
            int u1 = scan.nextInt();
            int u2 = scan.nextInt();
            int w = scan.nextInt();
            g.addEdge(u1-1,u2-1,w);
        }
        scan.close();
        
        g.primMST();
    }
    
    public static void main(String[] args)
    {
        //unittesting();
        fixroads();
    }
}
