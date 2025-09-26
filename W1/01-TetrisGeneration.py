numOfTestCases = input()

for i in range(int(numOfTestCases)):
    line = input().strip()
    length = len(line)
    tetrisSet = set()

    # Case 1: Length under 7, so just check if there is only a single duplicate or less.
    # This one is a special case, careful treatment is required.
    if length < 7:
        counter = 0
        for k in range(length):
            if line[k] not in tetrisSet:
                tetrisSet.add(line[k])
            else:
                counter += 1

        if counter > 1:
            print(0)
            continue # jump to next line
        else:
            print(1)
            continue # jump to next line

    # Case 2: Length over 7, if double -> take note of its location and skip to Step 2
    index = 0
    for k in range(7):
        if line[k] not in tetrisSet:
            tetrisSet.add(line[k])
        else:
            index = k

    # Assuming that we did hit Case 2, then...

    # Step 1: Parse 7 inputs repeatedly and check with set.
    # If we have a duplicate, print 0 and abort current line
    flag = True
    for j in range(index, length):
        currentTetrisSetCount = (j - index) % 7

        if currentTetrisSetCount == 0:
            tetrisSet.clear()

        if line[j] not in tetrisSet:
            tetrisSet.add(line[j])
        else:
            flag = False

    # Step 3: Print
    if flag:
        print(1)
    else:
        print(0)
