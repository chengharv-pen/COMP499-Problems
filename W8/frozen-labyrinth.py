"""

    Problem X of this week's lab, found it harder than Problem Y

"""

from collections import deque

def main():
    n, m = map(int, input().strip().split(' '))
    # print(n, m)

    # char arrays
    V = [''] * (n * m) # array representing the maze
    O = [''] * (n * m) # array that holds the directions

    # int arrays
    C = [0] * (n * m) # checked
    D = [0] * (n * m) # array that holds the amount of previous pointers left
    P = [0] * (n * m) # array that holds previous indexes

    a = 0 # location of A
    b = 0 # location of B

    # STEP 1
    # Filling array entries
    for i in range(n):
        s = input().strip()
        # print(s)

        for j in range(len(s)):
            V[i*m+j] = s[j]
            C[i*m+j] = 0 # 0 white
            D[i*m+j] = -1 # -1 means infinity
            P[i*m+j] = -1  # -1 means NIL

            if s[j] == 'A':
                a = i*m+j

            if s[j] == 'B':
                b = i*m+j


    # STEP 2
    q = deque()
    q.append(a)
    C[a] = 1
    D[a] = 0

    # 4 neighbours
    directions = (1, -1, m, -m)
    dirc = "RLDU"


    # while there are positions in queue and B not found...
    success = False
    while len(q) > 0 and not success:
        e = q.popleft()

        r = e // m      # integer division as intended in the C++ code, row index
        c = e % m       # column index

        # iterate through each direction, for current position popped from queue
        for j in range(4):

            # out of bounds check at current position
            if ((j == 0 and c == m - 1) or      # cannot go right
                (j == 1 and c == 0) or          # cannot go left
                (j == 2 and r == n - 1) or      # cannot go down
                (j == 3 and r == 0)):           # cannot go up
                continue

            # commit to 1 direction
            doWhileFlag = False
            nei = e + directions[j]
            while V[nei] == '.' or V[nei] == 'B' and not success:
                # if not the first move towards directions[j]
                if doWhileFlag:
                    r_recalc = nei // m
                    c_recalc = nei % m

                    # out of bounds check at shifted position
                    if ((j == 0 and c_recalc == m - 1) or  # cannot go right
                        (j == 1 and c_recalc == 0) or  # cannot go left
                        (j == 2 and r_recalc == n - 1) or  # cannot go down
                        (j == 3 and r_recalc == 0)):  # cannot go up

                        if C[nei] == 0:
                            q.append(nei)
                            C[nei] = 1
                            D[nei] = 1 + D[e]
                            P[nei] = e
                            O[nei] = dirc[j]

                        if V[nei] == 'B':
                            success = True

                        break

                    nei += directions[j]

                # if the first move towards directions[j]
                else:
                    doWhileFlag = True

                # hitting a wall
                if V[nei] == '#':
                    if C[nei - directions[j]] == 0:
                        q.append(nei - directions[j])
                        C[nei - directions[j]] = 1
                        D[nei - directions[j]] = 1 + D[e]
                        P[nei - directions[j]] = e
                        O[nei - directions[j]] = dirc[j]

                    if V[nei - directions[j]] == 'B':
                        success = True

                # if-else
            # while 2
        # for-loop directions[j]
    # while 1

    count = 0
    prev = P[b]
    while prev > -1:
        count += 1
        prev = P[prev]

    if count > 0:
        print("YES")
        print(count)
    else:
        print("NO")


if __name__ == "__main__":
    main()