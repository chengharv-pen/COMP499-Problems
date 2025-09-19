def main():
    while True:
        # 1 <= N <= 1000
        N = int(input().strip())

        if N == -1:
            break

        # Step 1: Populate intervals list and ASC sort it by finish time
        intervals = []
        for i in range(N):
            s, f, e = map(int, input().strip().split())
            intervals.append([s, f, e, i]) # triple (start, finish, enjoyment) followed by unsorted index.

        sorted_intervals = sorted(intervals, key=lambda x: (x[1], x[0])) # sort by finish, then start

        # DEBUG: printing intervals
        # print(intervals)
        # print(sorted_intervals)

        # Step 2: Initialize data structures
        D = [0] * N                 # sum of weight up to entry
        before = [-1] * N           # pointer to previous intervals
        decision = [0] * N          # 1 -> take interval, 0 -> do not take interval

        # Step 3: Find the maximum sums of weights (D)
        for i in range(N):
            for j in range(i):
                # if previous interval's finish time is <= current interval's start time...
                if sorted_intervals[j][1] <= sorted_intervals[i][0]:
                    before[i] = j

            include = sorted_intervals[i][2] + D[before[i]] if before[i] != -1 else sorted_intervals[i][2]
            exclude = D[i - 1] if i > 0 else 0

            D[i] = max(include, exclude)

            # consistent with D[i] being the max...
            if include > exclude: # if tied then DO NOT take interval
                decision[i] = 1
            else:
                decision[i] = 0

        # Step 4: Append decision indexes to result
        ind = N - 1
        result = []
        while ind >= 0:
            if decision[ind] == 1:
                result.append(sorted_intervals[ind][3])
                ind = before[ind]
            else:
                ind -= 1

        result.sort()
        print(f"{D[N - 1]}: {' '.join(map(str, result))}")

if __name__ == '__main__':
    main()