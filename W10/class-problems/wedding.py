"""

    Faulty output for now, would have to check with teacher tmrw

"""
from collections import deque

DEBUG_LEVEL = 3
dfs_order = deque()

def dfs_visit(first_visit, v: int, adj: list[list[int]], visited: list[int], visit: int) -> None:
    if not first_visit:
        visited[v] = visit

    for neighbor in adj[v]:
        if visited[neighbor] == -1:

            if first_visit:
                visited[v] = visit

            dfs_visit(first_visit, neighbor, adj, visited, visit)

    if first_visit:
        dfs_order.append(v)

def negate_literal(lit: int, n: int) -> int:
    return (lit + n) % (2 * n)

def get_literal(token, n):
    # extract all numbers from token, and exclude the h/w character at the end
    num = int(token[:-1])
    if token[-1] == 'h':
        return num               # husband TRUE means sits with bride
    else:
        return num + n           # wife TRUE means sits with bride

def main():
    n, m = map(int, input().strip().split())
    N = 2 * n
    adj = [[] for _ in range(N)]
    adj_rev = [[] for _ in range(N)]

    for i in range(m):
        tok1, tok2 = map(str, input().strip().split())

        lit1 = get_literal(tok1, n)
        lit2 = get_literal(tok2, n)

        if DEBUG_LEVEL >= 1:
            print(f'pair {i}: {lit1} {lit2}')

        neg_lit1 = negate_literal(lit1, n)
        neg_lit2 = negate_literal(lit2, n)

        print(neg_lit1, neg_lit2)

        # Encode (¬lit1 ∨ ¬lit2)
        # Construct implication graph
        adj[lit1].append(neg_lit2)
        adj[lit2].append(neg_lit1)

        # Construct transpose/reverse
        adj_rev[neg_lit2].append(lit1)
        adj_rev[neg_lit1].append(lit2)

    # encode clause (x_0)
    # literal 0 must be TRUE, so (¬0 → 0)
    adj[negate_literal(0, n)].append(0)
    adj_rev[0].append(negate_literal(0, n))

    if DEBUG_LEVEL >= 2:
        print()
        print("Implication Graph:")
        print(adj)
        print("Reverse of Implication Graph:")
        print(adj_rev)
        print()

    # Run the first DFS
    visited = [-1] * N

    for i in range(N):
        if visited[i] == -1:
            dfs_visit(True, i, adj, visited, 1)

    # Run the second DFS
    comp = [-1] * N # COMPONENTS
    comp_id = 0

    while dfs_order:
        v = dfs_order.pop()
        if comp[v] == -1:
            dfs_visit(False, v, adj_rev, comp, comp_id)
            comp_id += 1

    if DEBUG_LEVEL >= 3:
        print(dfs_order)
        print(comp)
        print(list(reversed(comp)))

    # ----- Check for contradictions -----
    for i in range(n):
        if comp[i] == comp[i+n]:
            print("bad luck")
            return

    # ----- Extract assignment -----
    # literal with larger SCC id = FALSE
    truth = [False] * n
    for i in range(n):
        truth[i] = comp[i] > comp[i+n]

    # Output people on bride's side for couples 1..n-1
    result = []
    for i in range(1, n):
        if truth[i]:
            result.append(f"{i}h")
        else:
            result.append(f"{i}w")

    print(" ".join(result))

if __name__ == '__main__':
    main()
