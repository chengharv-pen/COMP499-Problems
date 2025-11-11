from collections import deque

def main():
    n, k = map(int, input().strip().split())
    adj = [[] for _ in range(n)]

    for i in range(n):
        data = list(map(int, input().split()))
        s = data[0]
        for u in data[1:]:
            u -= 1
            adj[u].append(i)  # edge (u -> i) in reversed graph

    # run BFS from every villager
    # BE CAREFUL, THE INDENTATION REALLY MATTERS THIS TIME
    for v in range(n):
        # run BFS from v
        visited = [False] * n
        q = deque()

        # initialize BFS: q contains the current wave frontier
        q.append(v)
        visited[v] = True

        while q:
            cur = q.popleft()
            for neighbor in adj[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

        # compute how many were visited
        count = 0
        for i in range(n):
            if visited[i]:
                count += 1

        if count > k:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()