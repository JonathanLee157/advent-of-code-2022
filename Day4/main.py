def part_one():
    overlaps = 0

    with open("input.txt", "r+") as f:
        for line in f.readlines():
            line.strip("\n")
            if int(line.split("-")[0]) <= int(line.split("-")[1].split(",")[1]) and int(line.split("-")[2]) <= int(line.split("-")[1].split(",")[0]) or int(line.split("-")[0]) >= int(line.split("-")[1].split(",")[1]) and int(line.split("-")[2]) >= int(line.split("-")[1].split(",")[0]):
                overlaps += 1

    return overlaps

def part_two():
    overlaps = 0

    with open("input.txt", "r+") as f:
        for line in f.readlines():
            line.strip("\n")
            list1 = range(int(line.split("-")[0]), int(line.split("-")[1].split(",")[0]) + 1)
            list2 = range(int(line.split("-")[1].split(",")[1]), int(line.split("-")[2]) + 1)
            for val in list1:
                if val in list2:
                    overlaps += 1
                    break

    return overlaps

print(part_one())
print(part_two())