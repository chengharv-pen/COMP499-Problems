'''

    This was my solution for this problem,
    reused the code from simple-maze.py as a template

'''

from collections import deque

def main():
    n, m = map(int, input().strip().split(' '))

    # char arrays
    V = [''] * (n * m) # array representing the maze
    O = [''] * (n * m) # array that holds the directions

    # int arrays
    C = [0] * (n * m) # checked
    D = [0] * (n * m) # array that holds the amount of previous pointers left
    P = [0] * (n * m) # array that holds previous indexes

    a = 0 # location of A
    b = 0 # location of B

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

    success = False
    while len(q) > 0 and not success:
        e = q.popleft()

        r = e // m      # integer division as intended in the C++ code, row index
        c = e % m       # column index
        for j in range(4):

            borderFlag = False
            nei = e + directions[j]

            # HANDLE THE BORDER CASE FOR HORIZONTAL WRAP-AROUND
            # 1. Right border, moving to the right
            if j == 0 and c == m - 1 and V[e] in ['.', 'B', 'A'] and V[(r*m)] in ['.', 'B']:
                nei = (r * m)
                borderFlag = True

            # 2. Left border, moving to the left
            if j == 1 and c == 0 and V[e] in ['.', 'B', 'A'] and V[(r * m) + (m - 1)] in ['.', 'B']:
                nei = (r * m) + (m - 1)
                borderFlag = True

            # HANDLE THE BORDER CASES FOR VERTICAL WRAP-AROUND
            # 1. Bottom border, moving to the bottom
            if j == 2 and r == n - 1 and V[e] in ['.', 'B', 'A'] and V[c] in ['.', 'B']:
                nei = c
                borderFlag = True

            # 2. Top border, moving to the top
            if j == 3 and r == 0 and V[e] in ['.', 'B', 'A'] and V[((n - 1) * m) + c] in ['.', 'B']:
                nei = ((n - 1) * m) + c
                borderFlag = True

            # is this just checking for out of bounds? yes.
            if ((j == 0 and c == m - 1) or     # cannot go right
                (j == 1 and c == 0) or          # cannot go left
                (j == 2 and r == n - 1) or      # cannot go down
                (j == 3 and r == 0)) and not borderFlag: # cannot go up
                continue

            if V[nei] == '.' or V[nei] == 'B':
                if C[nei] == 0:
                    q.append(nei)
                    C[nei] = 1
                    D[nei] = 1 + D[e]
                    P[nei] = e
                    O[nei] = dirc[j]

            if V[nei] == 'B':
                success = True
                break

    # we just want to print the length of the shortest path
    currPointer = P[b]
    prev = 0
    count = 0
    while currPointer > -1:
        prev = currPointer
        currPointer = P[currPointer]
        count += 1

    # this final check should work...
    if count > 0 and a == prev:
        print("YES")
        print(count)
    else:
        print("NO")


if __name__ == "__main__":
    main()