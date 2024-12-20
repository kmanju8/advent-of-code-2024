grid = {}
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = set()


def traverse(loc, plant):
    visited.add(loc)

    border = 0
    area = 1
    for d in directions:
        loc2 = (loc[0] + d[0], loc[1] + d[1])
        if loc2 not in grid or grid[loc2] != plant:
            border += 1
            continue

        if loc2 not in visited:
            p, a = traverse(loc2, plant)
            border += p
            area += a

    return border, area



with open("input.txt", "r") as f:
    y = -1
    for line in f:
        clean = line.strip()
        y += 1
        for x in range(len(clean)):
            grid[(x, y)] = clean[x]

out = 0
for loc, plant in grid.items():
    if loc not in visited:
        p, a = traverse(loc, plant)
        out += p * a


print(out)
