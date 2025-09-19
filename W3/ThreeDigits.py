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


# find the 3 digits before trailing zeroes

# what if the case of less than 3 digits???
# case of >= 3 digits is free

# solution is based on len(factorial), but you need to compute the factorial itself...
# which may take a while