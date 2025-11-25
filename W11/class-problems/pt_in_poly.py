"""

    https://open.kattis.com/problems/pointinpolygon

"""

def subtract(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])

def det(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

def norm_sq(p):
    return p[0] * p[0] + p[1] * p[1]

def main():
    while True:
        line = input().strip()
        if not line:
            break
        n = int(line)
        if n == 0:
            break

        poly = []
        for _ in range(n):
            x, y = map(int, input().split())
            poly.append((x, y))

        # close polygon
        poly.append(poly[0])

        m = int(input())
        for _ in range(m):
            x, y = map(int, input().split())
            count = 0
            on = False

            for i in range(n):
                # assign top/bottom (t = top point, b = bottom point)
                if (poly[i][1] > poly[i+1][1]) or \
                   (poly[i][1] == poly[i+1][1] and poly[i][0] < poly[i+1][0]):
                    t = poly[i]
                    b = poly[i+1]
                else:
                    t = poly[i+1]
                    b = poly[i]

                # point y outside vertical span
                if y < b[1] or y > t[1]:
                    continue

                # horizontal edge
                if b[1] == t[1]:
                    if x >= min(t[0], b[0]) and x <= max(t[0], b[0]):
                        on = True
                        break

                # check if point is exactly on top point
                elif y == t[1]:
                    if x == t[0]:
                        on = True
                        break

                # check if point is exactly on bottom point
                elif y == b[1]:
                    if x == b[0]:
                        on = True
                        break
                    elif x < b[0]:
                        count += 1

                else:
                    # general case ray intersection test
                    p = (x, y)
                    cp = det(subtract(b, t), subtract(p, t))
                    if cp == 0:
                        on = True
                        break
                    elif cp < 0:
                        count += 1

            if on:
                print("on")
            elif count % 2 == 1:
                print("in")
            else:
                print("out")

if __name__ == "__main__":
    main()