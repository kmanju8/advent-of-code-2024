directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


maze = {}
with open("input2.txt", "r") as f:
    y = -1
    for line in f:
        clean = line.strip()
        y += 1
        for x in range(len(clean)):
            match clean[x]:
                case "S":
                    for d in range(4):
                        maze[(x, y, d)] = float("inf")
                    maze[(x, y, 1)] = 0
                case "E":
                    end = [(x, y, d) for d in range(4)]
                    for d in range(4):
                        maze[(x, y, d)] = float("inf")
                case ".":
                    for d in range(4):
                        maze[(x, y, d)] = float("inf")
                case _:
                    continue

end = set(end)

tiles = 0

while len(maze)>0:
    node = min(maze, key=maze.get)
    if node in end:
        break

    straight_ahead = (
        node[0] + directions[node[2]][0],
        node[1] + directions[node[2]][1],
        node[2],
    )
    if straight_ahead in maze:
        maze[straight_ahead] = min(maze[straight_ahead], maze[node] + 1)

    anti = (node[0], node[1], (node[2] + 1) % 4)
    if anti in maze:
        maze[anti] = min(maze[anti], maze[node] + 1000)

    clock = (node[0], node[1], (node[2] - 1) % 4)
    if clock in maze:
        maze[clock] = min(maze[clock], maze[node] + 1000)

    del maze[node]


print(maze[node])

# 90460
