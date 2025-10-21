def min_moves(a, b):
    dp = [[0] * (b + 1) for _ in range(a + 1)]

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if i == j:
                dp[i][j] = 0  # already a square
            else:
                best = float('inf')

                # horizontal cuts
                for k in range(1, i // 2 + 1):
                    best = min(best, dp[k][j] + dp[i - k][j] + 1)

                # vertical cuts
                for k in range(1, j // 2 + 1):
                    best = min(best, dp[i][k] + dp[i][j - k] + 1)

                dp[i][j] = best

    return dp[a][b]


a, b = map(int, input().split())
print(min_moves(a, b))