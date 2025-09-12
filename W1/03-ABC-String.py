string = input()
charset = set()
result = 0

# loop continuously until nothing in string
while True:
    # updates for every pass through the current string
    charmap = [0] * len(string)

    # loop once through current string, make the longest subsequence possible
    for i, char in enumerate(string):
        # if charset full, reset
        if len(charset) == 3:
            charset.clear()

        # check if there’s still room to reach 3
        remaining_chars = len(string) - i
        if remaining_chars + len(charset) < 3:
            break

        # we know that there's enough room, so...
        if char not in charset:
            charset.add(char)
            charmap[i] += 1

    # Extract characters where the charmap has 0
    temp = ''
    for char, bit in zip(string, charmap):
        if bit == 0:
            temp = temp + char

    string = temp
    result += 1

    if len(string) == 0:
        break

print(result)