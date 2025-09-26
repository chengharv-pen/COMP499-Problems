import sys

class Episode:
    def __init__(self, s: int, f: int, e: int, idx: int):
        self.s = s
        self.f = f
        self.e = e
        self.idx = idx

    def __lt__(self, other): # same as the comparison function in the C++ code...
        return self.f < other.f

def main():
    while True:
        try:
            # number of episodes
            n = int(input().strip())
        except (ValueError, EOFError):
            break

        if n == -1:
            break

        # initialize episodes array
        episodes = []
        for i in range(n):
            s, f, e = map(int, input().split())
            episodes.append(Episode(s, f, e, i))

        episodes.sort()

        # initialize other data structures
        dp = [0] * n
        before = [-1] * n
        take_dp = [False] * n

        # compute before
        for i in range(n):
            j = i - 1
            for j in range(j, -1, -1):
                if episodes[j].f <= episodes[i].s:
                    break

            before[i] = j # -1 indicates nothing is before

        # compute DP
        for i in range(n):
            take = episodes[i].e
            if before[i] >= 0:
                take += dp[before[i]]

            skip = dp[i - 1] if i > 0 else 0

            if take > skip:
                dp[i] = take
                take_dp[i] = True
            else:
                dp[i] = skip
                take_dp[i] = False

        # find solutions by using take_dp array
        sol = []
        index = n - 1
        while index >= 0:
            while index >= 0 and not take_dp[index]:
                index -= 1

            if index < 0:
                break

            sol.append(episodes[index].idx)
            index = before[index] # so we're backtracking here!

        sol = sorted(sol)
        print(f"{dp[n - 1]}:", end="")

        for val in sol:
            print(f" {val}", end="")

        print()

if __name__ == "__main__":
    main()