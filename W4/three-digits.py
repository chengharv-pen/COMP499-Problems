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

        # multiply the remaining part to result, modulo 1000 keeps the last 3 digits
        result = (result * num) % 1000

    # why do we need to remove the excess???
    # because there are extra 2s not paired with 5 that are part of the actual number
    excess_2 = count_2 - count_5
    # print(count_2, count_5, excess_2) # DEBUG

    # multiply by 2^excess_2 modulo 1000 (because result may become over 3 digits again)
    for _ in range(excess_2):
        result = (result * 2) % 1000

    return result

def main():
    n = int(input().strip())
    result = last_three_digits_before_trailing_zeroes(n)
    print(result)


if __name__ == '__main__':
    main()


