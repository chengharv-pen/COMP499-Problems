from collections import deque

dfs_order = deque()
def dfs_visit(v, adj, visited, visit):
    for neighbor in adj[v]:
        if visited[neighbor] == -1:
            visited[neighbor] = visit
            dfs_visit(neighbor, adj,
                          visited, visit)
    dfs_order.append(v)

def negate_literal(lit, n):
    return (lit + n) % (2 * n)

def get_literal(token, n):
    # extract all numbers from token,
    # and exclude the h/w character at the end
    num = int(token[:-1])
    if token[-1] == 'h':
        return num
    else:
        return num + n

def main():
    n, m = map(int, input().strip().split())
    N = 2 * n
    adj = [[] for _ in range(N)]
    adj_rev = [[] for _ in range(N)]

    for i in range(m):
        tok1, tok2 = map(str, input().strip().split())
        lit1 = get_literal(tok1, n)
        lit2 = get_literal(tok2, n)
        neg_lit1 = negate_literal(lit1, n)
        neg_lit2 = negate_literal(lit2, n)

        # (lit1 → ¬lit2), (lit2 → ¬lit1)
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

    # Run the first DFS
    visited = [-1] * N
    dfs_order.clear()
    for i in range(N):
        if visited[i] == -1:
            visited[i] = 1
            dfs_visit(i, adj, visited, 1)

    # Run the second DFS
    comp = [-1] * N
    comp_id = 0
    dfs_order_rev = deque(dfs_order) # copy
    dfs_order.clear()
    for v in reversed(dfs_order_rev):
        if comp[v] == -1:
            comp[v] = comp_id
            dfs_visit(v, adj_rev,
                          comp, comp_id)
            comp_id += 1

    assignment = [False] * n
    is_sat = True
    for i in range(n):
        comp_i = int(comp[i])
        comp_neg_i = int(comp[negate_literal(i, n)])
        if comp_i == comp_neg_i:
            is_sat = False
            break
        elif comp_i > comp_neg_i:
            assignment[i] = True
        else:
            assignment[i] = False

    if not is_sat:
        print("bad luck")
    else:
        for i in range(1, n):
            print(f'{i}', end='')
            temp = ''
            if assignment[i]: temp = 'w'
            else: temp = 'h'
            print(temp, end='')

            if i < n-1:
                print(' ', end='')
            else:
                print()

if __name__ == '__main__':
    main()