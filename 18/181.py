directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
XY = 71
maze = set([(x, y) for x in range(XY) for y in range(XY)])
end = (XY - 1, XY - 1)
visited = set()
queue = []


def t(pos):
    visited.add(pos)
    queue.append(pos)

    depth = 0
    while queue:
        length = len(queue)
        for _ in range(length):
            x = queue.pop(0)
            if x == end:
                print(depth)

            for d in directions:
                pos2 = tuple(x[i] + d[i] for i in range(2))

                if pos2 not in visited and pos2 in maze:
                    visited.add(pos2)
                    queue.append(pos2)

        depth += 1


count = 0
visited = set()
with open("input.txt", "r") as f:
    for line in f:
        clean = tuple(int(x) for x in line.strip().split(","))
        maze.remove(clean)
        count += 1
        if count == 1024:
            break


t((0, 0))
