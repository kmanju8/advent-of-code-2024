def find_antinodes(locs: list[(int, int)]) -> list[(int, int)]:
    out = []
    i = 0
    for a in locs:
        i += 1
        for b in locs[i:]:
            out.append((2 * b[0] - a[0], 2 * b[1] - a[1]))
            out.append((2 * a[0] - b[0], 2 * a[1] - b[1]))

    return out


grid = {}
with open("input.txt", "r") as f:
    x = -1
    for line in f:
        x += 1
        line = line.strip()
        for y in range(len(line)):
            if line[y]=='.':
                continue
            if line[y] in grid:
                grid[line[y]].append((x, y))
            else:
                grid[line[y]] = [(x, y)]


antinodes = set()

for _, locs in grid.items():
    antinodes |= set(find_antinodes(locs))


filtered = [
    node
    for node in antinodes
    if node[0] >= 0 and node[1] >= 0 and node[0] <= x and node[1] <= y
]

print(len(filtered))
