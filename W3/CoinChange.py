def main():
    m, n = map(int, input().strip().split(' '))
    coins = list(map(int, input().strip().split(' ')))

    dp = [float('inf')] * (m+1)

    # Base Case: Number of ways to amount to 0 is 0
    dp[0] = 0

    # For each amount find the optimal solution in a bottom-up fashion
    for i in range(1, m+1, 1):
        # For each amount, find the number of coins needed to make it
        for j in range(0, n, 1):
            subProblemCoin = i - coins[j]

            # Only use the subproblem if >= 0
            if subProblemCoin > 0:
                dp[i] = min(dp[subProblemCoin] + 1, dp[i])


    if dp[m] != float('inf'):
        print(dp[m])
    else:
        print('-1')

if __name__ == '__main__':
    main()