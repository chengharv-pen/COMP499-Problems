def main():
    while True:
        # 1 <= N <= 1000
        N = int(input())

        if N == -1:
            break

        # Step 1: Populate intervals list and ASC sort it by finish time
        intervals = []
        for i in range(N):
            line = list(map(int, input().split()))
            intervals.append([line[0], line[1], line[2], i]) # triple (start, finish, enjoyment) followed by unsorted index.

        sorted_intervals = sorted(intervals, key=lambda x: (x[1], x[0])) # sort by finish, then start

        # DEBUG: printing intervals
        print(intervals)
        # print(sorted_intervals)

        # Step 2: Initialize data structures
        D = [0] * N                 # sum of weight up to entry
        before = [-1] * N           # pointer to previous intervals
        decision = [0] * N          # 1 -> take interval, 0 -> do not take interval

        # Step 3: Find the maximum sums of weights (D)
        for i in range(N):
            # we need to store the interval that maximizes enjoyment,
            # not just the last one that is compatible [if multiple j are compatible with i, it might miss the best one]
            # TODO: review why the best_value/best_prev approach works... or spend more time tracing the debugger [edit: nvm this makes sense]
            best_prev = -1
            best_value = 0

            for j in range(i):
                if sorted_intervals[j][1] <= sorted_intervals[i][0]:
                    if D[j] > best_value:
                        best_value = D[j]
                        best_prev = j

            before[i] = best_prev

            include = sorted_intervals[i][2] + D[best_prev] if best_prev != -1 else sorted_intervals[i][2]

            exclude = D[i - 1] if i > 0 else 0

            if include > exclude:
                D[i] = include
                decision[i] = 1
            else:
                D[i] = exclude
                decision[i] = 0

        # Step 4: Append decision indexes to result (NOTE: THIS IS RELATIVE TO SORTED INTERVALS INDEXES)
        ind = N - 1
        result = []
        while ind >= 0:
            if decision[ind] == 1:
                result.append(ind)
                ind = before[ind]
            else:
                ind = ind - 1

        # Step 5: Find the unsorted indexes and print
        real_result = []
        sum = 0
        for ind in result:
            real_result.append(sorted_intervals[ind][3])
            sum += sorted_intervals[ind][2]

        print(f"{sum}: {' '.join(map(str, sorted(real_result)))}")

if __name__ == '__main__':
    main()

# for j in range(i):
#     # if previous interval's finish time is <= current interval's start time...
#     if sorted_intervals[j][1] <= sorted_intervals[i][0]:
#         before[i] = j


# if (sorted_intervals[i][2] + D[before[i]]) > D[i - 1]:
#     decision[i] = 1  # take interval
# else:
#     decision[i] = 0  # skip interval
#
# D[i] = max(sorted_intervals[i][2] + D[before[i]], D[i - 1])