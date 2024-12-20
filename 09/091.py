inp = open("input.txt", "r").read().strip()

if len(inp)%2 == 0:
    print("watch out, ends in a space")

filesize = 0
space = 0
idright = -1

file = True
for c in inp:
    if file:
        idright += 1
        filesize += int(c)

    if not file:
        space += int(c)
    file = not file

# print(filesize, space, idright, file)
# last number is a file

ans = 0

loc=-1
i = -1
idleft = 0
file = True
y = -1
counter = int(inp[y])
print(counter)
while i < filesize:
    loc+=1
    # print(int(inp[loc]))
    if file:
        for _ in range(int(inp[loc])):
            i+=1
            if not i < filesize:
                break
            print(i, idleft)
            ans += i*idleft
        idleft+=1
    else:
        for _ in range(int(inp[loc])):
            i+=1
            if not i < filesize:
                break

            ans += i*idright
            print(i, idright)
            counter-=1
            if counter < 1:
                idright-=1
                y-=2
                counter = int(inp[y])

    file = not file

print(ans, i, idleft, idright)

# 11501838184659 too high
# 8259840079543 too high
# 6398252054886