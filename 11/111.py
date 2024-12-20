def add_to_dict(d: dict, e: int, num: int):
    if e in d:
        d[e] += num
    else:
        d[e] = num


inp = open("input.txt", "r").read().strip().split()
stones = {int(i): 1 for i in inp}


for i in range(75):
    next_stones = {}

    for stone, num in stones.items():
        if stone == 0:
            add_to_dict(next_stones, 1, num)
            continue

        length = len(str(stone))
        if length % 2 == 0:
            a = int(str(stone)[: int(length / 2)])
            b = int(str(stone)[int(length / 2) :])
            add_to_dict(next_stones, a, num)
            add_to_dict(next_stones, b, num)
            continue

        add_to_dict(next_stones, stone * 2024, num)

    stones = next_stones
    # print(stones)

total = 0
for _, num in stones.items():
    total += num

print(total)
