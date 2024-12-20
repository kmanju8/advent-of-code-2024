file = open("input.txt", "r")
lines = file.readlines()
reg = [int(i.strip()[12:]) for i in lines[0:3]]
p = [int(i) for i in lines[4].strip()[9:].split(",")]

ip = 0
out = ""

# reg[0]=273342800000000

def combo(n):
    if n < 4:
        return n
    if n < 7:
        return reg[n - 4]
    print("Combo 7 found")
    return 7


def inst(n, op):
    global ip
    global out
    match n:
        case 0:
            reg[0] //= 2 ** combo(op)
        case 1:
            reg[1] ^= op
        case 2:
            reg[1] = combo(op) % 8
        case 3:
            ip = op - 2 if reg[0] != 0 else ip
        case 4:
            reg[1] ^= reg[2]
        case 5:
            out += str(combo(op) % 8)+","
        case 6:
            reg[1] = reg[0] // (2 ** combo(op))
        case 7:
            reg[2] = reg[0] // (2 ** combo(op))


end = len(p)
count = 0
while ip < end:
    print(count)
    inst(p[ip], p[ip + 1])
    ip += 2
    count +=1

print(out[:-1])
