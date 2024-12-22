modfactor = 2**24 - 1


def inc_dic(d, key, val):
    if key in d:
        d[key] += val
    else:
        d[key] = val


def step1(i):
    return ((i << 6) ^ i) & modfactor


def step2(i):
    return ((i >> 5) ^ i) & modfactor


def step3(i):
    return ((i << 11) ^ i) & modfactor


outs = {}

out = 0
with open("input.txt", "r") as f:
    history = []
    for line in f:
        x = int(line.strip())

        visited = set()
        for i in range(2000):
            y = step3(step2(step1(x)))

            history.append(y % 10 - x % 10)
            if len(history) >= 4:
                history = history[1:5] if len(history) == 5 else history
                history_tuple = tuple(history)

                if history_tuple not in visited:
                    visited.add(history_tuple)
                    inc_dic(outs, history_tuple, y % 10)

            x = y


a = max(outs, key=outs.get)
print(a, outs[a])
