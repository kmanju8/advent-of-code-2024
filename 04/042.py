with open("input.txt", "r") as f:
    grid = [[c for c in line if c != "\n"] for line in f]

count = 0
for i in range(len(grid)-2):
    for j in range(len(grid[0])-2):
        if grid[i+1][j+1]!='A':
            continue

        if not ((grid[i][j]=='M' and grid[i+2][j+2]=='S') or (grid[i][j]=='S' and grid[i+2][j+2]=='M')):
            continue

        if not ((grid[i+2][j]=='M' and grid[i][j+2]=='S') or (grid[i+2][j]=='S' and grid[i][j+2]=='M')):
            continue

        count+=1

print(count)
