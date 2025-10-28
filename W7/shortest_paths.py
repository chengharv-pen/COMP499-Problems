import heapq

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def main():
    n, m = map(int, input().strip().split(' '))

    adj = [[] for i in range(n)]

    for i in range(m):
        u, v, w = map(int, input().strip().split(' '))

        adj[u - 1].append(Pair(v - 1, w))
        adj[v - 1].append(Pair(u - 1, w))

    pq = []
    src = 0 # Taking vertex 0 as source

    # Create a vector for keys and initialize all
    # keys as infinite (INF)
    INF = float('inf')
    distance = [INF] * n
    processed = [0] * n

    # Insert source itself in priority queue and
    # initialize its key as 0.
    distance[0] = 0
    heapq.heappush(pq, Pair(0, src))

    while pq:
        d, u = heapq.heappop(pq)

        if processed[u] != 0:
            continue

        for i in adj[u]:
            v = i.first
            weight = i.second

            if processed[v] == 0 and weight + distance[u] < distance[v]:
                distance[v] = weight + distance[u]
                heapq.heappush(pq, Pair(v, distance[v]))

    for i in range(n):
        print(distance[i], end=' ')

if __name__ == "__main__":
    main()