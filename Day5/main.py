def part_one():
    stack_list = []
    stack_list.append(['Z', 'T', 'F', 'R', 'W', 'J', 'G'])
    stack_list.append(['G', 'W', 'M'])
    stack_list.append(['J', 'N', 'H', 'G'])
    stack_list.append(['J', 'R', 'C', 'N', 'W'])
    stack_list.append(['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'])
    stack_list.append(['S', 'R', 'T', 'D', 'V', 'W', 'C'])
    stack_list.append(['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'])
    stack_list.append(['S', 'J', 'N', 'M', 'G', 'C'])
    stack_list.append(['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L'])
    result = ""
    
    with open("input.txt", "r+") as f:
        lines = f.readlines()[10:]

    for line in lines:
        line = line.strip("\n")
        split = line.split(" ")
        i = int(split[1])
        _from = int(split[3])
        _to = int(split[5])
        for _ in range(i):
            temp = stack_list[_from - 1].pop()
            stack_list[_to - 1].append(temp)
    for l in stack_list:
        result += l.pop()
    
    return result


def part_two():
    stack_list = []
    stack_list.append(['Z', 'T', 'F', 'R', 'W', 'J', 'G'])
    stack_list.append(['G', 'W', 'M'])
    stack_list.append(['J', 'N', 'H', 'G'])
    stack_list.append(['J', 'R', 'C', 'N', 'W'])
    stack_list.append(['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'])
    stack_list.append(['S', 'R', 'T', 'D', 'V', 'W', 'C'])
    stack_list.append(['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'])
    stack_list.append(['S', 'J', 'N', 'M', 'G', 'C'])
    stack_list.append(['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L'])
    result = ""
    
    with open("input.txt", "r+") as f:
        lines = f.readlines()[10:]

    for line in lines:
        line = line.strip("\n")
        split = line.split(" ")
        i = int(split[1])
        _from = int(split[3])
        _to = int(split[5])
        temp_list = []
        for _ in range(i):
            temp = stack_list[_from - 1].pop()
            temp_list.append(temp)
        temp_list.reverse()
        stack_list[_to - 1] += temp_list
    for l in stack_list:
        result += l.pop()
    
    return result

print(part_one())
print(part_two())