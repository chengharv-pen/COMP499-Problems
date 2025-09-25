import math

def main():
    n = int(input().strip())
    array = list(map(int, input().strip().split(" ")))
    k = int(input().strip())

    ans = 0

    for i in range(len(array)):
        temp = array[i]
        for j in range(i, n):
            temp = math.gcd(temp, array[j])
            if temp == k:
                ans += 1
            elif temp < k:
                break

    print(ans)

if __name__ == "__main__":
    main()