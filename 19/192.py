i1 = "input.txt"
i2 = "input2.txt"

patterns = [i.strip() for i in open(i1, "r").read().split(",")]


towel_cache = {}


def towel_possible(t):
    if t in towel_cache:
        return towel_cache[t]

    if t == "":
        return 1

    valid = 0
    for p in patterns:
        if t.startswith(p):
            valid += towel_possible(t[len(p) :])

    if t not in towel_cache:
        towel_cache[t] = valid

    return valid


out = 0
with open(i2, "r") as f:
    for line in f:
        clean_towel = line.strip()
        out += towel_possible(clean_towel)

print(out)
