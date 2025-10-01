def main():
    n = int(input().strip()) - 1
    dims = list(map(int, input().split()))

    # minimum scalar multiplications for A_i to A_j
    dp = [[0] * n for _ in range(n)]

    # Chain length from 2 to n
    for length in range(2, n + 1):

        # slides a window of size = length across the chain
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            """
            
            Tries all possible split points k inside subchain (Ai .. Aj)
            
            For each split, you add:

            1. Cost of multiplying the left subchain dp[i][k].
            
            2. Cost of multiplying the right subchain dp[k+1][j].
            
            3. Cost of multiplying the resulting two matrices together:
                dims[i] * dims[k + 1] * dims[j + 1]
                
            Then take the minimum of all splits
            
            """
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    print(dp[0][n - 1])

if __name__ == '__main__':
    main()