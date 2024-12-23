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


def unpack(pattern):
    out = ""
    for i in range(len(pattern) - 1):
        out += dir_combis[(pattern[i], pattern[i + 1])]

    return out


out = 0
with open("input2.txt", "r") as f:
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

        for i in range(5):
            pattern = unpack("A" + pattern)

        print(len(pattern), num_value)
        out += len(pattern) * num_value

print(out)
