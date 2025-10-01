# O(n log n) solution here please.
from bisect import bisect_left
from collections import deque


def lis_length_only(A):
    tail = []
    for num in A:
        idx = bisect_left(tail, num)
        if idx == len(tail):
            tail.append(num)
        else:
            tail[idx] = num
    return len(tail)

def main():
    while True:
        N = int(input())
        if N == -1:
            break

        A = list(map(int, input().split()))

        dp = [0] * N  # dp[i]: length of LIS ending at A[i]
        prev = [0] * N  # prev[i]: index of previous element in LIS
        tail = []  # stores end values of LIS of each length
        tail_indices = []  # stores indices corresponding to values in 'tail'

        for i in range(N):
            idx = bisect_left(tail, A[i])
            if idx == len(tail):
                tail.append(A[i])
                tail_indices.append(i)
            else:
                tail[idx] = A[i]
                tail_indices[idx] = i

            dp[i] = idx + 1
            if idx == 0:
                prev[i] = i
            else:
                prev[i] = tail_indices[idx - 1]

        # Find index of last element of LIS
        max_len = max(dp)
        ind = dp.index(max_len)

        # Backtrack to reconstruct LIS (by indices)
        result = deque()
        result.appendleft(ind)
        while prev[ind] != ind:
            ind = prev[ind]
            result.appendleft(ind)

        # Print indices
        print(f"{len(result)}: {' '.join(map(str, result))}")


if __name__ == '__main__':
    main()