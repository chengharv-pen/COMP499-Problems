import heapq
import time

def prim_with_forced_edge(n, adj, a, b, w):
    """
    Compute MST cost using Prim's algorithm, forcing edge (a,b,w) to be included.

    Time Complexity: O(m^2 log n)
    """
    visited = [False] * (n + 1)
    pq = []
    total_cost = w
    visited[a] = True
    visited[b] = True
    added = 2

    # Add edges from both endpoints of the forced edge
    for v, w2 in adj[a]:
        if not visited[v]:
            heapq.heappush(pq, (w2, v))
    for v, w2 in adj[b]:
        if not visited[v]:
            heapq.heappush(pq, (w2, v))

    # Prim's algorithm loop
    while pq and added < n:
        w2, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += w2
        added += 1
        for v, w3 in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (w3, v))

    return total_cost


def main():
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        edges.append((a, b, w))
        adj[a].append((b, w))
        adj[b].append((a, w))

    results = []
    for (a, b, w) in edges:
        results.append(str(prim_with_forced_edge(n, adj, a, b, w)))

    print("\n".join(results))


if __name__ == "__main__":
    start = time.time()
    main()
    print("Time: ", time.time() - start)