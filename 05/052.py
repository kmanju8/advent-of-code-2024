from functools import cmp_to_key

temp = {}
with open("a.txt", "r") as f:
    for line in f:
        a = line.strip().split("|")
        if a[1] in temp:
            temp[a[1]].add(a[0])
        else:
            temp[a[1]] = set([a[0]])


def customsort(a, b):
    if b in temp and a in temp[b]:
        return -1
    if a in temp and b in temp[a]:
        return 1
    else:
        return 0


cuskey = cmp_to_key(customsort)

count = 0
with open("b.txt", "r") as f:
    for line in f:
        seq = line.strip().split(",")

        corrected = sorted(seq, key=cuskey)
        if seq != corrected:
            mid = int(corrected[int((len(corrected)) / 2)])
            count += mid
print(count)
