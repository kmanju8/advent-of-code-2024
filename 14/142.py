X = 101
Y = 103
T = 0
LIM = 10404
dt = [1008, 3941, 1149, 4305]


def max_in_single_y(board):
    out = {i: 0 for i in range(Y)}

    for loc, _ in board.items():
        out[loc[1]] += 1

    return out[max(out, key=out.get)]


def count_in_range(lx, hx, ly, hy, board):
    filtered = [
        v
        for loc, v in board.items()
        if loc[0] >= lx and loc[0] <= hx and loc[1] >= ly and loc[1] <= hy
    ]
    return sum(filtered)


def print_board(b):
    c = {i: 0 for i, v in b.items() if v > 0}
    out = [list(["."] * X) for _ in range(Y)]

    for loc in c:
        out[loc[1]][loc[0]] = "X"

    for row in out:
        print("".join(row))


def is_tree(b):
    left = set([loc for loc, v in b.items() if loc[0] <= 49 and v > 0])
    right = set(
        [((X - 1) - loc[0], loc[1]) for loc, v in b.items() if loc[0] >= 51 and v > 0]
    )

    # 250 would be fully symmetric
    return len(left & right) > 150


while T < LIM:
    T += 1
    board = {}
    with open("input.txt", "r") as f:
        for line in f:
            temp = [int(i) for i in line.split(",")]
            final_loc = ((temp[0] + T * temp[2]) % X, (temp[1] + T * temp[3]) % Y)

            board[final_loc] = 1

    if max_in_single_y(board) > 30:
        print(max_in_single_y(board))
        print(T)
        print_board(board)


print(T)
