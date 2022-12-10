import string

def part_one():
    letters = []
    lines = []
    alphabet = list(string.ascii_letters)
    priority = 0

    with open("input.txt", "r+") as f:
        for line in f.readlines():
            lines.append(line.strip("\n"))
            
        for line in lines:
            first_half = line[:len(line)//2]
            second_half = line[len(line)//2:]
            for c in first_half:
                if c in second_half:
                    letters.append(c)
                    break

        for c in letters:
            priority += alphabet.index(c) + 1

        return priority    

def part_two():
    letters = []
    lines = []
    alphabet = list(string.ascii_letters)
    priority = 0

    with open("input.txt", "r+") as f:
        for line in f.readlines():
            lines.append(line.strip("\n"))
            
        for i in range(0, len(lines)-2, 3):
            for c in lines[i]:
                if c in lines[i + 1] and c in lines[i + 2]:
                    letters.append(c)
                    break
        
                    priority += alphabet.index(c) + 1

        return priority

print(part_one())
print(part_two())