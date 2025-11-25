"""

    https://open.kattis.com/problems/convexhull

"""

def subtract(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])

def det(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

def norm_sq(p):
    return p[0] * p[0] + p[1] * p[1]

# Global pivot point P
P = (0, 0)

def custom_comp(p1, p2):
    cp = det(subtract(p1, P), subtract(p2, P))
    if cp == 0:
        return norm_sq(subtract(p1, P)) < norm_sq(subtract(p2, P))
    return cp > 0

# Python sort does not accept comparator directly → wrap with key function
from functools import cmp_to_key

def print_ch(pts):
    print(len(pts))
    for x, y in pts:
        print(x, y)

def main():
    while True:
        try:
            n = int(input())
        except:
            break
        if n == 0:
            break

        pts = []
        global P
        P = None

        for i in range(n):
            x, y = map(int, input().split())
            if P is None or y < P[1] or (y == P[1] and x < P[0]):
                P = (x, y)
            pts.append((x, y))

        # eliminate duplicates
        pts.sort()
        unique_pts = []
        for p in pts:
            if not unique_pts or p != unique_pts[-1]:
                unique_pts.append(p)
        pts = unique_pts
        n = len(pts)

        if n <= 2:
            print_ch(pts)
            continue

        # sort by custom comparator
        pts.sort(key=cmp_to_key(lambda a, b: -1 if custom_comp(a, b) else (1 if custom_comp(b, a) else 0)))

        # build hull (incomplete)
        res = [pts[0], pts[1]]

        for i in range(2, len(pts)):
            # missing loop logic
            # while res[end-2], res[end-1], pts[i] makes a right turn:
            #     pop res[-1]
            pass

        print_ch(res)

if __name__ == '__main__':
    main()