from collections import deque


def main():
    while True:
        N = int(input())
        if N == -1:
            break

        A = list(map(int, input().split()))
        dp = [1] * N
        prev = [0] * N

        for i in range(N):
            m = 0
            prev[i] = i
            for j in range(i):
                if A[j] < A[i] and dp[j] > m:
                    m = dp[j]
                    prev[i] = j

            dp[i] = 1 + m

        result = deque()
        ind = dp.index(max(dp))

        result.appendleft(ind)
        while prev[ind] != ind:
            ind = prev[ind]
            result.appendleft(ind)

        # Print indices
        print(f"{len(result)}: {' '.join(map(str, result))}")


if __name__ == '__main__':
    main()
