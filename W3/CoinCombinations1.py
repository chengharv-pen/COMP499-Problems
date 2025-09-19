# Output: 8
def main():
    m, n = map(int, input().strip().split(' '))
    coins = list(map(int, input().strip().split(' ')))

    dp = [0] * (m + 1) # Each entry corresponds to amount of ways to sum to <index>

    # Base case: there is one way to sum to index 0
    dp[0] = 1

    # Each amount is the subproblem
    for i in range(1, m + 1):
        for coin in coins:     # try each coin
            if i >= coin:
                dp[i] = (dp[i] + dp[i - coin]) % (10 ** 9 + 7)

    print(dp[m])

if __name__ == '__main__':
    main()

# import sys
#
#
# def main():
#     try:
#         m, n = map(int, sys.stdin.readline().strip().split())
#         coins = list(map(int, sys.stdin.readline().strip().split()))
#
#         if len(coins) != n:
#             print("Invalid input: expected", n, "coins, got", len(coins), file=sys.stderr)
#             return
#
#         if any(c <= 0 for c in coins):
#             print("Invalid coin value (must be > 0)", file=sys.stderr)
#             return
#
#         dp = [0] * (m + 1)
#         dp[0] = 1
#
#         for i in range(1, m + 1):
#             for coin in coins:
#                 if i >= coin:
#                     dp[i] = (dp[i] + dp[i - coin]) % (10 ** 9 + 7)
#
#         print(dp[m])
#
#     except Exception as e:
#         print("Run error:", e, file=sys.stderr)
#
#
# if __name__ == '__main__':
#     main()