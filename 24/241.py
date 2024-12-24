logic = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}


mem = {}
with open("start1.txt", "r") as f:
    for line in f:
        inp = line.strip().split(":")
        mem[inp[0]] = int(inp[1])

calc = {}
lastz = 0
with open("inst1.txt", "r") as f:
    for line in f:
        inp = line.strip().replace("-> ", "").split(" ")
        calc[inp[3]] = inp[:3]
        if inp[3][0] == "z":
            lastz = max(lastz, int(inp[3][1:]))


def logicize(addr, inst):
    val1 = mem[inst[0]] if inst[0] in mem else logicize(inst[0], calc[inst[0]])
    val2 = mem[inst[2]] if inst[2] in mem else logicize(inst[2], calc[inst[2]])

    ans = logic[inst[1]](val1, val2)
    if out not in mem:
        mem[out] = ans
    return ans


final = 0
for i in range(lastz, -1, -1):
    final = final << 1
    out = "z" + str(i) if len(str(i)) == 2 else "z0" + str(i)
    mem[out] = logicize(out, calc[out])
    final += mem[out]

print(bin(final))
