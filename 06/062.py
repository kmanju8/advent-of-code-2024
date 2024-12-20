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
                    start = (x, y)
                    boulder[(x, y)] = False
                case _:
                    boulder[(x, y)] = True

count = 0
for i, block in boulder.items():
    print(i, count)
    if i==start:
        continue

    tempboulder=dict(boulder)
    if not block:
        tempboulder[i]=True

    loc=start
    visited = set()
    boulders = set()
    dirindex = 0
    
    next_step = (loc[0] + directions[dirindex][0], loc[1] + directions[dirindex][1])
    while next_step in tempboulder:
        visited.add((loc[0], loc[1], dirindex))
        if tempboulder[next_step]:
            dirindex = (dirindex + 1) % 4
        else:
            loc = next_step
        next_step = (loc[0] + directions[dirindex][0], loc[1] + directions[dirindex][1])

        if (loc[0], loc[1], dirindex) in visited:
            count+=1
            break


print(count)

# 308 too low