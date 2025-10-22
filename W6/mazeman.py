from collections import deque

def main():
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    total_dots = sum(row.count('.') for row in grid)
    reachable_dots = 0
    entrances_used = 0

    def bfs(si, sj):
        q = deque([(si, sj)])
        visited[si][sj] = True
        count = 0
        while q:
            i, j = q.popleft()
            if grid[i][j] == '.':
                count += 1

            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                    if grid[ni][nj] in [' ', '.']:
                        visited[ni][nj] = True
                        q.append((ni, nj))
                    elif 'A' <= grid[ni][nj] <= 'W':
                        # mark letters (like entrances) as visited so they aren’t double-counted
                        visited[ni][nj] = True

        return count

    # find entrances on the border
    entrances = []
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n-1 or j == 0 or j == m-1):
                if 'A' <= grid[i][j] <= 'W':
                    entrances.append((i, j))

    for ei, ej in entrances:
        # start BFS from an adjacent open cell, not the letter itself
        for di, dj in dirs:
            ni, nj = ei + di, ej + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if grid[ni][nj] in [' ', '.']:
                    curr = bfs(ni, nj)
                    if curr > 0:
                        entrances_used += 1
                        reachable_dots += curr
                    break  # only need one BFS per connected region

    unreachable_dots = total_dots - reachable_dots
    print(entrances_used, unreachable_dots)

if __name__ == '__main__':
    main()