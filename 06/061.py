directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

boulder = {}
with open("input.txt", "r") as f:
    y = -1
    for line in f:
        clean = line.strip()
        y += 1
        for x in range(len(clean)):
            match clean[x]:
                case ".":
                    boulder[(x, y)] = False
                case "^":
                    loc = (x, y)
                    boulder[(x, y)] = False
                case _:
                    boulder[(x, y)] = True

visited = set()
dirindex = 0
next_step = (loc[0] + directions[dirindex][0], loc[1] + directions[dirindex][1])
while next_step in boulder:
    print(loc)
    visited.add(loc)
    if boulder[next_step]:
        dirindex = (dirindex + 1) % 4
    else:
        loc = next_step
    next_step = (loc[0] + directions[dirindex][0], loc[1] + directions[dirindex][1])

visited.add(loc)