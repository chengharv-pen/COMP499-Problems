import time
start = time.time()

string = input()
charset = set()
result = 0

# loop continuously until nothing in string
while len(string) > 0:
    # updates for every pass through the current string
    bitmap = [0] * len(string)

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
            bitmap[i] += 1

    # Extract characters where the bitmap has 0

    # Submission 1: This one creates a new string for every iteration... probably why I hit time limit
    # temp = ''
    # for char, bit in zip(string, bitmap):
    #     if bit == 0:
    #         temp = temp + char
    # string = temp

    # Builds a list of characters and then joins them into a single string at the end.
    # Submission 2: that did not give the extra time save we needed... the outer+inner loop must be the culprit O(N^2)
    string = ''.join([char for char, bit in zip(string, bitmap) if bit == 0])
    result += 1

print(result)

end = time.time()
print(f"Execution time: {end - start:.6f} seconds")