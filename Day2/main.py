def part_one():
    opp = []
    player = []
    score = 0

    with open("input.txt", "r+") as f:
        for line in f.readlines():
            opp.append(line[0])
            player.append(line[2])

    for i in range(len(opp)):
        if player[i] == 'X':
            score += 1
            if opp[i] == 'C':
                score += 6
            elif opp[i] == 'A':
                score += 3
        elif player[i] == 'Y':
            score += 2
            if opp[i] == 'A':
                score += 6
            elif opp[i] == 'B':
                score += 3
        elif player[i] == 'Z':
            score += 3
            if opp[i] == 'B':
                score += 6
            elif opp[i] == 'C':
                score += 3

    return score

def part_two():
    opp = []
    player = []
    score = 0

    with open("input.txt", "r+") as f:
        for line in f.readlines():
            opp.append(line[0])
            player.append(line[2])

    for i in range(len(opp)):
        if player[i] == 'X':
            if opp[i] == 'C':
                score += 2
            elif opp[i] == 'A':
                score += 3
            else:
                score += 1
        elif player[i] == 'Y':
            score += 3
            if opp[i] == 'A':
                score += 1
            elif opp[i] == 'B':
                score += 2
            else:
                score += 3
        elif player[i] == 'Z':
            score += 6
            if opp[i] == 'B':
                score += 3
            elif opp[i] == 'C':
                score += 1
            else:
                score += 2

    return score

print(part_one())
print(part_two())