# YES
# 4
# 1 2 4 7
# 3
# 3 5 6
import sys

# S = m(m+n)/2
def findSubset(index, currentSum, subset):
    if currentSum == halfSum:
        return True
    if currentSum > halfSum or index >= N:
        return False

    # Choose the current element
    subset.append(array[index])
    used[index] = True
    if findSubset(index + 1, currentSum + array[index], subset):
        return True

    # Backtrack
    subset.pop()
    used[index] = False

    # Skip the current element
    return findSubset(index + 1, currentSum, subset)


N = int(input())

array = []
for i in range(N):
    array.append(i + 1)

totalSum = N*(N+1)/2

if (totalSum % 2) == 1:
    print("NO")
    raise SystemExit
else:
    print("YES")

# i mean i could sliding window the sets away until it either finds or doesn't find...
# but time complexity n^2... probably not it


# for n = 7
# S = 28, S/2 = 14 (we're trying for 2 sets of 14 here)

# 7,6,1 = 14 // 2,3,4,5 = ?? = 14
# so start adding from the end numbers, until its really close to S/2, then find remainder using S/2 - currentSum
# ok so I tunnel visioned on iteration start-end, should consider end-start iterations...
# but also you can do the 14-sum by adding starting numbers, no need to backtrack in that case

# check the C++ file the teacher sends for non-recursive solution
halfSum = totalSum / 2
used = [False] * N
set1 = []

if findSubset(0, 0, set1):
    set2 = []
    for i in range(N):
        if not used[i]:
            set2.append(array[i])

    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)
