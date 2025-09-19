# Output: 13 7
#         17 10
def main():
    while True:
        check = input().strip()

        if check == '-1 -1':
            return

        # n being the number of skeleton types
        # d being the cost capacity
        n, d = map(int, check.split(' '))

        powers = []
        costs = []
        for i in range(n):
            power, cost = input().strip().split(' ')
            powers.append(int(power))
            costs.append(int(cost))

        # print(powers)
        # print(costs)

        # Initialize DP table
        # dp[c] = max power with cost c
        dp = [-1] * (d + 1)
        dp[0] = 0  # Base Case: 0 cost yields 0 power

        for i in range(n):
            p = powers[i]
            c = costs[i]

            # Subproblems... all cost capacities from d to c - 1
            for j in range(d, c - 1, -1):
                if dp[j - c] != -1:
                    dp[j] = max(dp[j], dp[j - c] + p) # this part needs reviewing...

        # Find the max power and corresponding min cost
        max_power = max(dp)
        min_cost = dp.index(max_power)

        print(f"{max_power} {min_cost}")


if __name__ == '__main__':
    main()