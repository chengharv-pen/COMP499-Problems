"""

    https://cses.fi/problemset/task/2189

"""

def det(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

def subtract(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])

def main():
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2, x3, y3 = map(int, input().split())
        p1 = (x1, y1)
        p2 = (x2, y2)
        p3 = (x3, y3)

        cp = det(subtract(p2, p1), subtract(p3, p1))

        if cp == 0:
            print("TOUCH")
        elif cp > 0:
            print("LEFT")
        else:
            print("RIGHT")

if __name__ == "__main__":
    main()