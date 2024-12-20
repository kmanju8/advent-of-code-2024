X = 101
Y = 103
T = 100
board = {(x, y): 0 for x in range(X) for y in range(Y)}


def count_in_range(lx, hx, ly, hy):
    filtered = [
        v
        for loc, v in board.items()
        if loc[0] >= lx and loc[0] <= hx and loc[1] >= ly and loc[1] <= hy
    ]
    return sum(filtered)


with open("input.txt", "r") as f:
    for line in f:
        temp = [int(i) for i in line.split(",")]
        final_loc = ((temp[0] + T * temp[2]) % X, (temp[1] + T * temp[3]) % Y)

        board[final_loc] += 1

nw = count_in_range(0, 49, 0, 50)
ne = count_in_range(51, X, 0, 50)
sw = count_in_range(0, 49, 52, Y)
se = count_in_range(51, X, 52, Y)

print(nw*ne*sw*se)
