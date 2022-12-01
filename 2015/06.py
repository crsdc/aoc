# https://adventofcode.com/2015/day/6

with open("06data.txt", "r") as datafile:
    input = datafile.readlines()

# Part 1

grid = [[False for i in range(1000)] for j in range(1000)]

for line in input:
    instruct = line.strip().replace('turn ','').replace(' through ', ' ').replace(' ',',').split(',')
    if instruct[0] == 'on':
        for x in range(int(instruct[1]), int(instruct[3]) + 1):
            for y in range(int(instruct[2]), int(instruct[4]) + 1):
                grid[x][y] = True
    if instruct[0] == 'off':
        for x in range(int(instruct[1]), int(instruct[3]) + 1):
            for y in range(int(instruct[2]), int(instruct[4]) + 1):
                grid[x][y] = False
    if instruct[0] == 'toggle':
        for x in range(int(instruct[1]), int(instruct[3]) + 1):
            for y in range(int(instruct[2]), int(instruct[4]) + 1):
                grid[x][y] = not grid[x][y]

total = 0
for x in range(len(grid)):
    total += grid[x].count(True)

print(total)

# Part 2

grid = [[0 for i in range(1000)] for j in range(1000)]

for line in input:
    instruct = line.strip().replace('turn ','').replace(' through ', ' ').replace(' ',',').split(',')
    for x in range(int(instruct[1]), int(instruct[3]) + 1):
        for y in range(int(instruct[2]), int(instruct[4]) + 1):
            if instruct[0] == 'on':
                grid[x][y] += 1
            elif instruct[0] == 'off' and grid[x][y] > 0:
                grid[x][y] -= 1
            elif instruct[0] == 'toggle':
                grid[x][y] += 2

total = 0
for x in range(len(grid)):
    total += sum(grid[x])

print(total)