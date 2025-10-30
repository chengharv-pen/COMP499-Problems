"""

    Problem Y of this week's lab

"""

import heapq

def dijkstra(n, adj, src):
    dist = [float('inf')] * n
    dist[src] = 0
    string_dist = [''] * n
    string_dist[src] = '0'

    pq = [(0, src)]  # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:  # Skip outdated entry
            continue
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                string_dist[v] = str(d + w)
                heapq.heappush(pq, (dist[v], v))
    return dist, string_dist

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a - 1].append((b - 1, c))
        adj[b - 1].append((a - 1, c))

    dist, string_dist = dijkstra(n, adj, 0)

    res = ' '.join(string_dist)
    print(res)

if __name__ == '__main__':
    main()