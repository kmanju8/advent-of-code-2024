directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def twod(x):
    return (x[0], x[1])


maze = {}
route_to = {}
with open("input.txt", "r") as f:
    y = -1
    for line in f:
        clean = line.strip()
        y += 1
        for x in range(len(clean)):
            match clean[x]:
                case "S":
                    for d in range(4):
                        maze[(x, y, d)] = float("inf")
                        route_to[(x, y, d)] = set()
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

X = x
Y = y


def print_board(b):
    c = {i: 0 for i in b}
    out = [list(["."] * X) for _ in range(Y)]

    for loc in c:
        out[loc[1]][loc[0]] = "O"

    for row in out:
        print("".join(row))


tiles = 0


while len(maze) > 0:
    node = min(maze, key=maze.get)
    # print(node)

    # if node in end:
    #     break

    straight_ahead = (
        node[0] + directions[node[2]][0],
        node[1] + directions[node[2]][1],
        node[2],
    )

    if straight_ahead in maze:
        if maze[node] + 1 < maze[straight_ahead]:
            route_to[straight_ahead] = set(route_to[node])
            route_to[straight_ahead].add(twod(node))
        if maze[node] + 1 == maze[straight_ahead]:
            route_to[straight_ahead] = set(route_to[straight_ahead] | route_to[node])
            route_to[straight_ahead].add(twod(node))
        maze[straight_ahead] = min(maze[straight_ahead], maze[node] + 1)

    anti = (node[0], node[1], (node[2] + 1) % 4)
    if anti in maze:
        maze[anti] = min(maze[anti], maze[node] + 1000)
        route_to[anti] = route_to[node]

    clock = (node[0], node[1], (node[2] - 1) % 4)
    if clock in maze:
        maze[clock] = min(maze[clock], maze[node] + 1000)
        route_to[clock] = route_to[node]

    del maze[node]


# print(maze[node])

print(len(route_to[end[0]])+1)

# print_board(route_to[end[0]])

# 90460
