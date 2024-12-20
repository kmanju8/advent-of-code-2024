grid = {}
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def traverse(loc, height, visited):
    if grid[loc] != height:
        return

    if height == 9:
        visited.add(loc)
        return

    for d in directions:
        loc2 = (loc[0] + d[0], loc[1] + d[1])
        if loc2 in grid:
            traverse(loc2, height + 1, visited)


with open("input.txt", "r") as f:
    y = -1
    for line in f:
        clean = line.strip()
        y += 1
        for x in range(len(clean)):
            grid[(x, y)] = int(clean[x])

out = 0
for loc, height in grid.items():
    if height == 0:
        visited = set()
        traverse(loc, height, visited)
        out+=len(visited)


print(out)

# 81 total routes to a 9
# 1541


# 746