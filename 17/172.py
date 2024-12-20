file = open("input.txt", "r")
lines = file.readlines()
reg = [int(i.strip()[12:]) for i in lines[0:3]]
p = [int(i) for i in lines[4].strip()[9:].split(",")]


out = ""
ip = 0
reg[0] = 117440


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
            out += str(combo(op) % 8) + ","
        case 6:
            reg[1] = reg[0] // (2 ** combo(op))
        case 7:
            reg[2] = reg[0] // (2 ** combo(op))


# 190615597416320 lower
# 190352950558720 upper


count = 190615597416320
bound = 8**16
inc = 1
# while out != "2,4,1,2,7,5,0":
while count < bound:
    reg[0] = count
    reg[1] = 0
    reg[2] = 0

    out = ""
    ip = 0

    end = len(p)
    while ip < end:
        # print(count)
        inst(p[ip], p[ip + 1])
        ip += 2

    # seqcheck = "2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0,"
    seqcheck = "2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0,"
    if out[-len(seqcheck) :] == seqcheck:
        print(count, out[:-1])
        break

    # print(count, out, len(out))
    count += inc



# 190615638981647 too high
# 190615638936497
# 190615638785039 also too high
# 190615597431823 correct