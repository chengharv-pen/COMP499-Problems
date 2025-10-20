def main():
    # let the input be n
    # we want to count the number of substractions until n is 0
    # substractions are done using digits of current n

    n = int(input().strip())
    print(n)

    dp = [0] * (n + 1)

    # 27 -> 20 -> 18 -> 10 -> 9 -> 0
    while n != 0:
        digits = list(str(n))
        print(digits)

        maximum = 0
        for i in range(len(digits)):
            if int(digits[i]) > maximum:
                maximum = int(digits[i])

        n = n - maximum
        dp[n] += 1


    res = 0
    for i in range(len(dp)):
        res += dp[i]

    print(res)


if __name__ == '__main__':
    main()