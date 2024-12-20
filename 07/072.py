def check(target, current, remaining):
    if len(remaining) == 0:
        return current == target

    if current > target:
        return False

    return check(target, current + remaining[0], list(remaining[1:])) or check(
        target, current * remaining[0], list(remaining[1:])
    ) or check(
        target, int(str(current) + str(remaining[0])), list(remaining[1:])
    )


with open("input.txt", "r") as f:
    eqs = [[int(x) for x in line.strip().split()] for line in f]

count = 0
for ops in eqs:
    if check(ops[0], ops[1], list(ops[2:])):
        # print(target)
        count += ops[0]

print(count)
