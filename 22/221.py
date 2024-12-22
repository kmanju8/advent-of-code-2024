modfactor = 2**24 - 1


def step1(i):
    return ((i << 6) ^ i) & modfactor


def step2(i):
    return ((i >> 5) ^ i) & modfactor


def step3(i):
    return ((i << 11) ^ i) & modfactor

out = 0
with open("input.txt", "r") as f:
    for line in f:
        x = int(line.strip())

        for i in range(2000):
            x = step3(step2(step1(x)))

        out += x

print(out)
