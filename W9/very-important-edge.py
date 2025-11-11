"""

    Non-TLE solution
    Had a slightly different solution and missed a single test case because of TLE

    The intended time limit is 20 seconds, not 3 seconds.

"""

import heapq

def prim(n, start, adj, special):
    visited = [False] * (n + 1)
    pq = [(0, start)]  # (weight, start_node)
    total_cost = 0

    while pq:
        w, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        total_cost += w

        for v, wt in adj[u]:
            if (u, v, wt) == special or (v, u, wt) == special:
                continue
            elif not visited[v]:
                heapq.heappush(pq, (wt, v))

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

    ans = -1
    for e in edges:
        ans = max(ans, prim(n, 1, adj, e))

    print(ans)

if __name__ == '__main__':
    main()