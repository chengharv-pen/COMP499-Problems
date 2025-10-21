def main():
    n = int(input().strip())
    MOD = 10 ** 9 + 7

    S = n * (n + 1) // 2

    if S % 2 == 1:
        print(0)
        return

    target = S // 2

    dp = [0] * (target + 1)
    dp[0] = 1

    # iterate through numbers 1 to n
    for x in range(1, n + 1):
        # iterate sums backwards to avoid reuse of x multiple times
        for s in range(target, x - 1, -1):
            dp[s] = (dp[s] + dp[s - x]) % MOD # pls verify why this works...

    # dp[target] counts ordered choices (A vs B), so divide by 2
    inv2 = pow(2, MOD - 2, MOD)

    print(dp[target] * inv2 % MOD)


if __name__ == "__main__":
    main()
