from itertools import pairwise

def is_monatomic(seq):
    return all((x < y) for x, y in pairwise(seq)) or all((x > y) for x, y in pairwise(seq))


def is_close(seq):
    return all(abs(x - y) <= 3 for x, y in pairwise(seq))


safe = 0
with open("input.txt", "r") as f:
    for line in f:
        row = [int(num) for num in line.split()]
        for i in range(len(row)):
            temp=row[:i]+row[i+1:]
            if is_monatomic(temp) and is_close(temp):
                safe += 1
                break

# brute forcing it but hey