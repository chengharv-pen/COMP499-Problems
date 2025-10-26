
import java.util.*;


class Pair {
    int first, second;
    public Pair(int first, int second)
    {
        this.first = first;
        this.second = second;
    }
}

public class shortest_paths {


    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();

        List<List<Pair> > adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for(int i=0;i<m;i=i+1){
            int u = scan.nextInt();
            int v = scan.nextInt();
            int w = scan.nextInt();

            adj.get(u-1).add(new Pair(v-1, w));
            adj.get(v-1).add(new Pair(u-1, w));
        }
        scan.close();


        PriorityQueue<Pair> pq = new PriorityQueue<>(
            n, new Comparator<Pair>() {
                public int compare(Pair a, Pair b)
                {
                    return a.second - b.second;
                }
            });

        int src = 0; // Taking vertex 0 as source

        // Create a vector for keys and initialize all
        // keys as infinite (INF)
        int INF = Integer.MAX_VALUE;
        int[] distance = new int[n];
        Arrays.fill(distance, INF);
        int[] processed = new int[n];
        Arrays.fill(processed, 0);

        // Insert source itself in priority queue and
        // initialize its key as 0.
        distance[0] = 0;
        pq.offer(new Pair(0, 0));

        while (!pq.isEmpty()) {
            int u = pq.peek().first;
            int d = pq.peek().second;
            pq.poll();

            if(processed[u]!=0)
                continue;

            for (Pair i : adj.get(u)) {
                int v = i.first;
                int weight = i.second;

                if(processed[v]==0 && weight+distance[u]<distance[v]){
                    distance[v] = weight+distance[u];
                    pq.offer(new Pair(v, distance[v]));
                }

          }// for
        }// while

        for(int i=0;i<n;++i){
            System.out.print(distance[i] + " ");
        }

    }
}