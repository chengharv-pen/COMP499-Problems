# Output: 3
def main():
    m, n = map(int, input().strip().split(' '))
    coins = list(map(int, input().strip().split(' ')))

    dp = [0] * (m + 1) # Each entry corresponds to amount of ways to sum to <index>

    # Base case: there is one way to sum to index 0
    dp[0] = 1

    # Each coin is the subproblem
    for coin in coins:
        for i in range(coin, m + 1):
            dp[i] = (dp[i] + dp[i - coin]) % (10 ** 9 + 7)

    print(dp[m])

if __name__ == '__main__':
    main()