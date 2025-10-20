from functools import lru_cache

@lru_cache(maxsize=None)
def min_moves(a, b):
    # base case: already a square
    if a == b:
        return 0

    best = float('inf')

    # try horizontal cuts
    for i in range(1, a // 2 + 1):
        best = min(best, min_moves(i, b) + min_moves(a - i, b) + 1)

    # try vertical cuts
    for j in range(1, b // 2 + 1):
        best = min(best, min_moves(a, j) + min_moves(a, b - j) + 1)

    return best

a, b = map(int, input().split())
print(min_moves(a, b))