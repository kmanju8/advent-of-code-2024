grid = {}
with open("input.txt", "r") as f:
    x = -1
    for line in f:
        x += 1
        line = line.strip()
        for y in range(len(line)):
            if line[y] == ".":
                continue
            if line[y] in grid:
                grid[line[y]].append((x, y))
            else:
                grid[line[y]] = [(x, y)]


def find_antinodes(locs: list[(int, int)]) -> list[(int, int)]:
    out = []
    i = 0
    for a in locs:
        i += 1
        for b in locs[i:]:
            change_vec = (b[0] - a[0], b[1] - a[1])

            start = b
            while start[0] >= 0 and start[1] >= 0 and start[0] <= x and start[1] <= y:
                out.append(start)
                start = (start[0] + change_vec[0], start[1] + change_vec[1])

            start = b
            while start[0] >= 0 and start[1] >= 0 and start[0] <= x and start[1] <= y:
                out.append(start)
                start = (start[0] - change_vec[0], start[1] - change_vec[1])

    return out


antinodes = set()

for _, locs in grid.items():
    antinodes |= set(find_antinodes(locs))

print(len(antinodes))
