# see Legendre's formula for factorial trailing zeros
def count_trailing_zeros(n: int) -> int:
    count = 0
    i = 5

    while i <= n:
        count += n // i # floor division
        i *= 5

    return count

factorial = int(input())
print(count_trailing_zeros(factorial))