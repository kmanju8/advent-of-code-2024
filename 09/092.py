inp = open("input.txt", "r").read().strip()

if len(inp)%2 == 0:
    print("watch out, ends in a space")

file = True
files=[]
i=0
fileid=0
for c in inp:
    if file:
        files.append((i,int(c),fileid))
        fileid+=1
    i+=int(c)
    file = not file

copy = list(files)
copy.reverse()

for element in copy:
    i=0
    while files[i][0]<element[0]:
        if element[1]<=files[i+1][0]-(files[i][0]+files[i][1]):
            new = [x for x in files if x[2]!=element[2]]
            files = new[:i+1] + [(new[i][0]+new[i][1],element[1],element[2])] + new[i+1:]
            break
        i+=1


out = 0
for x in files:
    for i in range(x[0],x[0]+x[1]):
        out += i * x[2]

print(out)
