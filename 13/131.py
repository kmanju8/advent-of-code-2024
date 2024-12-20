import re


with open("input.txt", "r") as f:
    count = 3
    prize = []
    out = 0
    for line in f:
        count = (count + 1) % 4
        match count:
            case 0:
                buttonmatch = re.search(r"Button A: X\+(\d+), Y\+(\d+)", line)
                a = int(buttonmatch.group(1))
                c = int(buttonmatch.group(2))
            case 1:
                buttonmatch = re.search(r"Button B: X\+(\d+), Y\+(\d+)", line)
                b = int(buttonmatch.group(1))
                d = int(buttonmatch.group(2))
            case 2:
                prize_match = re.search(r"Prize: X=(\d+), Y=(\d+)", line)
                prize.append(int(prize_match.group(1))+10000000000000)
                prize.append(int(prize_match.group(2))+10000000000000)

                invdet = a * d - b * c
                if invdet == 0:
                    print("shit")
                x = (d * prize[0] - b * prize[1]) / invdet
                y = (a * prize[1] - c * prize[0]) / invdet

                if x.is_integer() and y.is_integer():
                    out += 3 * int(x) + int(y)
            case _:
                flatmat = []
                prize = []

print(out)
