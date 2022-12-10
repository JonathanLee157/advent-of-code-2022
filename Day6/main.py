def part_one():
    with open("input.txt", "r", encoding="utf-8") as f:
        packet = f.readline().strip("\n")
    for i in range(len(packet)):
        if len(packet[i:i + 4]) == len(set(packet[i:i + 4])):
            return i + 4
        

def part_two():
    with open("input.txt", "r", encoding="utf-8") as f:
        packet = f.readline().strip("\n")
    for i in range(len(packet)):
        if len(packet[i:i + 14]) == len(set(packet[i:i + 14])):
            return i + 14

print(part_one())
print(part_two())