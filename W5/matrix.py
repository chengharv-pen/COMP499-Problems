def matrix_chain_order(dims):
    n = len(dims) - 1  # Number of matrices
    # dp[i][j] = minimum scalar multiplications for A_i to A_j
    dp = [[0] * n for _ in range(n)]

    # Chain length from 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]


# Example usage:
dimensions = [5, 10, 3, 12, 5]  # Matrices: A(5×10), B(10×3), C(3×12), D(12×5)
min_mults = matrix_chain_order(dimensions)
print(f"Minimum scalar multiplications: {min_mults}")  # Output: 405