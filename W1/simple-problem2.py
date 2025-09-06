def find_equal_sum_subsets(N):
    total = N * (N + 1) // 2

    if total % 2 != 0:
        print("NO")
        return

    target = total // 2
    subset1 = []
    subset2 = []

    # Greedy approach: pick largest numbers first for subset1
    for num in range(N, 0, -1):
        if target - num >= 0:
            subset1.append(num)
            target -= num
        else:
            subset2.append(num)

    print("YES")
    print(len(subset1))
    print(' '.join(map(str, subset1)))
    print(len(subset2))
    print(' '.join(map(str, subset2)))

def find_equal_sum_subsets_forward(N):
    total = N * (N + 1) // 2

    if total % 2 != 0:
        print("NO")
        return

    target = total // 2
    subset1 = []
    subset2 = []

    for i in range(1, N + 1):
        if i <= target:
            subset1.append(i)
            target -= i
        else:
            subset2.append(i)

    print("YES")
    print(len(subset1))
    print(' '.join(map(str, subset1)))
    print(len(subset2))
    print(' '.join(map(str, subset2)))

N = int(input())
find_equal_sum_subsets(N)
find_equal_sum_subsets_forward(N)