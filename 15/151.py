directions = {"v": (0, 1), ">": (1, 0), "^": (0, -1), "<": (-1, 0)}
i1 = "input.txt"
i2 = "input2.txt"

box = {}
with open(i1, "r") as f:
    y = -1
    for line in f:
        clean = line.strip()
        y += 1
        for x in range(len(clean)):
            match clean[x]:
                case ".":
                    box[(x, y)] = False
                case "@":
                    loc = (x, y)
                    box[(x, y)] = False
                case "O":
                    box[(x, y)] = True
                case _:
                    pass

seq = open(i2, "r").read().strip()


for d in seq:
    loc2 = (loc[0] + directions[d][0], loc[1] + directions[d][1])

    valid = True
    new_positions_to_add = []
    to_test = [loc]  # test if they're in valid places, then use to queue up next iter
    while len(to_test) > 0:
        next_set = []
        for x in to_test:
            n = (x[0] + directions[d][0], x[1] + directions[d][1])
            if n not in box:
                valid = False
                break

            if box[n]:
                next_set.append(n)

        new_positions_to_add += to_test
        to_test = next_set

    if not valid:
        continue

    new_vals = {}
    for pos in new_positions_to_add:
        next_loc = (pos[0] + directions[d][0], pos[1] + directions[d][1])
        new_vals[next_loc] = box[pos]
        box[pos] = False
    for pos, val in new_vals.items():
        box[pos] = val
    loc = loc2


out = 0
for k, boulder in box.items():
    if boulder:
        out += k[0] + k[1] * 100
print(len([i for i, v in box.items() if v]), out)


# 1413675 right answer
