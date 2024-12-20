def write_to(path, grid):
    with open(path, "w") as f:
        for line in grid:
            f.write(f"{''.join(line)}\n")


with open("input.txt", "r") as f:
    grid = [[c for c in line if c != "\n"] for line in f]

grid90 = [[row[i] for row in grid] for i in range(len(grid[0]))]
for i in grid90:
    i.reverse()


# grid45
grid45 = [[] for i in range(len(grid) + len(grid[0]))]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        grid45[i + j].append(grid[i][j])

grid135 = [[] for i in range(len(grid90) + len(grid90[0]))]
for i in range(len(grid90)):
    for j in range(len(grid90[0])):
        grid135[i + j].append(grid90[i][j])


write_to("input45.txt", grid45)
write_to("input90.txt", grid90)
write_to("input135.txt", grid135)
