from itertools import pairwise

def is_monatomic(seq):
    return all((x < y) for x, y in pairwise(seq)) or all((x > y) for x, y in pairwise(seq))


def is_close(seq):
    return all(abs(x - y) <= 3 for x, y in pairwise(seq))


safe = 0
with open("input.txt", "r") as f:
    for line in f:
        row = [int(num) for num in line.split()]
        if is_monatomic(row) and is_close(row):
            safe += 1


print(safe)
