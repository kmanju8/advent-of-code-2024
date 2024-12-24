# solved in a more investagative fashion.
# realised that each digit is calculated with every gate from the digit before it
# plus 2 new ANDs, 1 OR and 2 XORs.
# looked for diffs between sets of gates used in each calculation,
# then manually sorted them into the regular structure addition needs
currentz = 0
visited = {i: set() for i in range(50)}

mem = {}
original = set()
with open("start1.txt", "r") as f:
    for line in f:
        inp = line.strip().split(":")
        mem[inp[0]] = inp[0]
        original.add(inp[0])

calc = {}
lastz = 0
with open("inst1.txt", "r") as f:
    for line in f:
        inp = line.strip().replace("-> ", "").split(" ")
        calc[inp[3]] = inp[:3]
        if inp[3][0] == "z":
            lastz = max(lastz, int(inp[3][1:]))


def logicize(addr, inst):
    global currentz
    global visited

    val1 = mem[inst[0]] if inst[0] in mem else logicize(inst[0], calc[inst[0]])
    val2 = mem[inst[2]] if inst[2] in mem else logicize(inst[2], calc[inst[2]])

    visited[currentz].add(inst[1] + " " + addr)
    ans = [addr + inst[1], val1, val2]

    if out not in mem:
        mem[out] = ans
    return ans


memo = {j: [] for j in range(lastz + 1)}
final = 0
for i in range(lastz, -1, -1):
    currentz = i
    out = "z" + str(i) if len(str(i)) == 2 else "z0" + str(i)
    mem[out] = logicize(out, calc[out])


for i in range(lastz):
    print(sorted(list(visited[i + 1] - visited[i])))


# dodgy lines
# 08 09 vvr z08
# 16 17 rnq bkr
# 28 29 tfb z28
# 39 40 z39 mqh

# print(",".join(sorted("vvr z08 rnq bkr tfb z28 z39 mqh".split(" "))))
