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
        e = q[0]
        q.popleft()

        r = e // m      # integer division as intended in the C++ code, row index
        c = e % m       # column index
        for j in range(4):

            # is this just checking for out of bounds? yes.
            if ((j == 0 and c == m - 1) or      # cannot go right
                (j == 1 and c == 0) or          # cannot go left
                (j == 2 and r == n - 1) or      # cannot go down
                (j == 3 and r == 0)):           # cannot go up
                continue

            nei = e + directions[j]

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

    if success:
        print("YES")
        print(D[b])

        os = ''
        while b != a:
            os += O[b]
            b = P[b]

        res = ''
        for i in range(len(os) - 1, -1, -1):
            res += os[i]

        print(res)
    else:
        print("NO")


if __name__ == "__main__":
    main()