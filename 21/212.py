directions = {
    ">": (-1, 0),
    "v": (0, -1),
    "^": (0, 1),
    "<": (1, 0),
}  # ordering of this really matters - as it changes ordering of dfs result
opposite = {"v": "^", "<": ">", ">": "<", "^": "v"}
keypad = {((i - 1) % 3, 2 - ((i - 1) // 3)): str(i) for i in range(1, 10)}
keypad[(1, 3)] = "0"
keypad[(2, 3)] = "A"
rev_keypad = {v: k for k, v in keypad.items()}

dirpad = {(0, 1): "<", (1, 0): "^", (2, 1): ">", (1, 1): "v", (2, 0): "A"}
rev_dirpad = {v: k for k, v in dirpad.items()}


def dfs(grid, start, end, visited):
    if start == end:
        return [""]
    routes = []
    visited.add(grid[end])
    for sym, d in directions.items():
        pp = (end[0] + d[0], end[1] + d[1])
        if pp in grid and grid[pp] not in visited:
            for path in dfs(grid, start, pp, visited.copy()):
                if opposite[sym] not in path:
                    if len(path) > 1 and (sym in path and sym != path[-1]):
                        continue
                    routes.append(path + sym)

    return routes


dir_combis = {
    (x, y): dfs(dirpad, rev_dirpad[x], rev_dirpad[y], set())[0] + "A"
    for x in rev_dirpad
    for y in rev_dirpad
}


def next_pad(move_count):
    temp = {k: 0 for k in dir_combis}
    for k, v in move_count.items():
        temp[("A", dir_combis[k][0])] += v
        for i in range(len(dir_combis[k]) - 1):
            temp[(dir_combis[k][i], dir_combis[k][i + 1])] += v

    return temp


out = 0
with open("input.txt", "r") as f:
    for line in f:
        num_value = int(line.strip()[:-1])
        clean = "A" + line.strip()
        pattern = ""

        for i in range(len(clean) - 1):
            a = dfs(keypad, rev_keypad[clean[i]], rev_keypad[clean[i + 1]], set())
            pat = a[0]
            for s in a:
                if s[0] == "<":
                    pat = s
                if s[-1] == ">":
                    pat = s

            pattern += pat + "A"

        start = ("A", pattern[0])
        button_move_count = {k: 0 for k in dir_combis}
        button_move_count[start] += 1
        for i in range(len(pattern) - 1):
            button_move_count[(pattern[i], pattern[i + 1])] += 1

        for i in range(25):
            button_move_count = next_pad(button_move_count)

        min_len = 0
        for k, v in button_move_count.items():
            min_len += v

        print(min_len, num_value, min_len * num_value)
        out += min_len * num_value

print(out)
