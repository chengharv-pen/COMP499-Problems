from functools import lru_cache

@lru_cache(maxsize=None)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    # divisible by 2 (rule out ALL even numbers)
    if n % 2 == 0:
        return False

    # everything else...
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False

    return True

def goldbach_pairs(even_number):
    pairs = []
    for i in range(2, even_number // 2 + 1):
        if is_prime(i) and is_prime(even_number - i):
            pairs.append((i, even_number - i))
    return pairs

def main():
    n = int(input().strip())

    for i in range(n):
        number = int(input().strip())
        pairs = goldbach_pairs(number)

        print(f"{number} has {len(pairs)} representation(s)")
        for a, b in pairs:
            print(f"{a}+{b}")
        print()


if __name__ == '__main__':
    main()