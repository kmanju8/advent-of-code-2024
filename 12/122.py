grid = {}
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
corner_check = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
visited = set()


def same_as_current(loc, plant):
    return loc in grid and grid[loc] == plant


def traverse(loc, plant):
    visited.add(loc)

    corner = 0
    for c in corner_check:
        loc3 = (loc[0] + c[0], loc[1] + c[1])
        loc4 = (loc[0], loc[1] + c[1])
        loc5 = (loc[0] + c[0], loc[1])

        same_diag = same_as_current(loc3, plant)

        conda = same_as_current(loc4, plant)
        condb = same_as_current(loc5, plant)
        same_adj = conda and condb  # same adj probably wrong
        if conda != condb:
            continue

        if not (same_diag and same_adj):
            corner += 1

    area = 1
    for d in directions:
        loc2 = (loc[0] + d[0], loc[1] + d[1])
        if loc2 not in visited and loc2 in grid and grid[loc2] == plant:
            p, a = traverse(loc2, plant)
            corner += p
            area += a

    return corner, area


# let's count corners
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


# AA
# AB same adj and diff diag


# AB
# BB diff adj and diff diag

# AB
# BA diff adj and same diag


# la moire: not(same adj AND same diag)
# also make sure to skip if adj cells are diff from each other
