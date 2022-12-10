def part_one():
    max = 0
    current = 0

    with open("input.txt", "r+") as f:
        for line in f.readlines():
            if line == "\n":
                if max < current:
                    max = current
                current = 0
            else:
                current += int(line.strip("\n"))
    return max

def part_two():
    top3 = [0, 0, 0]
    current = 0

    with open("input.txt", "r+") as f:
        for line in f.readlines():
            if line == "\n":
                if current > top3[0] or current > top3[1] or current > top3[2]:
                    minimum = min(top3)
                    index = top3.index(minimum)
                    top3[index] = current
                current = 0
            else:
                current += int(line.strip("\n"))
    return sum(top3)

print(part_one())
print(part_two())