#Used help from Github user JasonCannon

def part_one():
    sgn = lambda x: (x > 0) - (x < 0)
    h, t = (0, 0), (0, 0)
    D, Seen = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}, {t}

    with open("input.txt", "r") as f: 
        for args in map(lambda x: x.strip().split(), f.readlines()):
            d, v = args[0], int(args[1])
            for _ in range(v):
                h = tuple(sum(x) for x in zip(h, D[d]))
                dx, dy = h[0] - t[0], h[1] - t[1]
                if abs(dx) > 1 or abs(dy) > 1:
                    t = tuple(sum(x) for x in zip(t, [sgn(dx), sgn(dy)]))
                Seen.add(t)

    return len(Seen)

def part_two():
    sgn = lambda x: (x > 0) - (x < 0)
    R = [(0, 0) for _ in range(10)]
    D, Seen = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}, {R[-1]}

    with open("input.txt", "r") as f:
        for args in map(lambda x: x.strip().split(), f.readlines()):
            d, v = args[0], int(args[1])
            for _ in range(v):
                R[0] = tuple(sum(x) for x in zip(R[0], D[d]))
                for i in range(1, len(R)):
                    dx, dy = R[i-1][0] - R[i][0], R[i-1][1] - R[i][1]
                    if abs(dx) > 1 or abs(dy) > 1:
                        R[i] = tuple(sum(x) for x in zip(R[i], [sgn(dx), sgn(dy)]))
                Seen.add(R[-1])

    return len(Seen)

print(part_one())
print(part_two())