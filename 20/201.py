import sys

sys.setrecursionlimit(10**5)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
distance = {}
maze = set()


def inc_dic(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1


def t(pos, depth):
    distance[pos] = depth

    for d in directions:
        np = (pos[0] + d[0], pos[1] + d[1])
        if np not in distance and np in maze:
            t(np, depth + 1)


with open("input.txt", "r") as f:
    y = -1
    for line in f:
        clean = line.strip()
        y += 1
        for x in range(len(clean)):
            match clean[x]:
                case "S":
                    maze.add((x, y))
                    start = (x, y)
                case "E":
                    maze.add((x, y))
                    end = (x, y)
                case ".":
                    maze.add((x, y))
                case _:
                    continue


t(start, 0)
# print(distance[end])

shortcuts = {}
for pos, time in distance.items():
    for d in directions:
        np = (pos[0] + d[0], pos[1] + d[1])
        if np not in maze:
            for e in directions:
                nnp = (np[0] + e[0], np[1] + e[1])
                if nnp in distance:
                    inc_dic(shortcuts, distance[pos] - distance[nnp])

clean_shortcuts = {k - 2: v for k, v in shortcuts.items() if k - 2 >= 100}

out = 0
for time, shortcuts in clean_shortcuts.items():
    out += shortcuts
print(out)
