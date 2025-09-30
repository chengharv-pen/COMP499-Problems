def main():
    """

    You can either:
    1. Add one character to the string
    2. Remove one character from the string
    3. Replace one character in the string

    Apparently this is a Dynamic Programming problem?????????? wtf?

    """
    # take input
    word1 = input().strip()
    word2 = input().strip()
    m = len(word1)
    n = len(word2)

    # initialize dp array
    dp = []
    for _ in range(m + 1):
        dp.append([0] * (n + 1))

    # Base Case 1: transform word1 into empty string
    for i in range(1, m + 1):
        dp[i][0] = i

    # Base Case 2: transform word2 into empty string
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]: # matching letters
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # replace, delete, insert
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    print(dp[m][n])



if __name__ == "__main__":
    main()