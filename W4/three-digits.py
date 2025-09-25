import math

def last_three_digits_before_trailing_zeroes(n):
    result = 1
    count_5 = 0
    count_2 = 0

    # looping from 1 to n is just how we manually build n!,
    # carefully removing the parts that create trailing zeroes and keeping only what we need.
    #
    # why are we removing factors of 5 and 2?
    # pairs of 5 and 2 make 10, which we need to remove...
    for i in range(1, n + 1):
        num = i

        # remove all factors of 5 and count them
        while num % 5 == 0:
            num //= 5
            count_5 += 1

        # remove all factors of 2 and count them
        while num % 2 == 0:
            num //= 2
            count_2 += 1

        result *= num

        # remove trailing zeroes after every multiplication
        while result % 10 == 0:
            result //= 10

        # keep result manageable (prevent overflows)
        result %= 10**10

    # why do we need to remove the excess???
    # because there are extra 2s not paired with 5 that are part of the actual number
    excess_2 = count_2 - count_5
    # print(count_2, count_5, excess_2) # DEBUG

    for _ in range(excess_2):
        result *= 2

        # remove trailing zeroes after every multiplication
        while result % 10 == 0:
            result //= 10

        # keep result manageable (prevent overflows)
        result %= 10**10

    result_str = str(result).rstrip('0') # convert to string and remove trailing zeroes
    last_digits = result_str[-3:] if len(result_str) >= 3 else result_str # get last 3 non-zero digits

    return last_digits

def main():
    n = int(input().strip())
    result = last_three_digits_before_trailing_zeroes(n)
    # print(result, math.factorial(n))
    print(result)


if __name__ == '__main__':
    main()


