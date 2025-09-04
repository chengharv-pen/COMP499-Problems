case_number = 1

while True:
    # b: number of ballots /// c: number of candidates
    b, c = map(int, input().split())
    if b == 0 and c == 0:
        break

    # ballots is a list of ballot... a ballot is also a list
    ballots = []
    for _ in range(b):
        line = input().split()
        ballot = list(map(int, line))
        ballots.append(ballot)

    # wins[i][j] = number of ballots where i is ranked higher than j
    wins = []
    for _ in range(c):
        wins.append([0] * c)


    for ballot in ballots:
        # lower index = higher rank
        position = [0] * c
        for rank, candidate in enumerate(ballot):
            position[candidate] = rank

        # count pairwise wins
        for i in range(c):
            for j in range(c):
                if i != j and position[i] < position[j]:
                    wins[i][j] += 1

    # check for Condorcet winner
    winner = -1
    for i in range(c):
        is_winner = True

        # compare current candidate (i) against other ones (j)
        # if there is a loss, it cannot be the winning candidate
        for j in range(c):
            if i != j and wins[i][j] <= b // 2: # floor division checks for majority vote
                is_winner = False
                break

        if is_winner:
            winner = i
            break

    if winner != -1:
        print(f"Case {case_number}: {winner}")
    else:
        print(f"Case {case_number}: No Condorcet winner")

    case_number += 1
