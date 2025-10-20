def main():
    n = int(input().strip())
    INF = 10**9

    dp = [INF] * (n + 1)
    dp[0] = 0

    for x in range(1, n + 1):
        t = x

        # extract digits without converting to string (faster)
        while t > 0:
            d = t % 10
            t //= 10

            if d == 0:
                continue

            dp[x] = min(dp[x], 1 + dp[x - d])

    print(dp[n])

if __name__ == "__main__":
    main()