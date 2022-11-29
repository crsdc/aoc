# https://adventofcode.com/2021/day/5

def countoverlaps(grid):
    overlaps = 0
    for x in range(1000):
        for y in range(1000):
            if grid[x][y] > 1:
                overlaps += 1
    print(overlaps)

with open('05data.txt', 'r') as datafile:
    inputlist = datafile.readlines()

grid = [[0 for i in range(1000)] for j in range(1000)]
linecoords = []
for line in inputlist:
    # Make each line a list of form [0 is x1,  1 is y1,  2 is x2,  3 is y2]
    linecoords.append(list(map(int, line.strip().replace(' -> ', ',').split(','))))

# Part 1
for line in linecoords:

    # Vertical lines, where x1 == x2
    if line[0] == line[2]:
        if line[3] > line[1]:
            linerange = range(line[1], line[3] + 1)
        else:
            linerange = range(line[3], line[1] + 1)
        for y in linerange:
            grid[line[0]][y] += 1

    # Horizontal lines, where y1 == y2
    elif line[1] == line[3]:
        if line[2] > line[0]:
            linerange = range(line[0], line[2] + 1)
        else:
            linerange = range(line[2], line[0] + 1)
        for x in linerange:
            grid[x][line[1]] += 1

countoverlaps(grid)

# Part 2
for line in linecoords:

    # Diagonal lines
    if (line[0] != line[2]) and (line[1] != line[3]):
        # Line can go in four directions from x1,y1 so find out which and draw
        # right and down
        if (line[2] > line[0]) and (line[3] > line[1]):
            for offset in range(line[2] - line[0] + 1):
                grid[line[0] + offset][line[1] + offset] += 1
        # left and down
        elif (line[0] > line[2]) and (line[3] > line[1]):
            for offset in range(line[0] - line[2] + 1):
                grid[line[0] - offset][line[1] + offset] += 1
        # right and up
        elif (line[2] > line[0]) and (line[1] > line[3]):
            for offset in range(line[2] - line[0] + 1):
                grid[line[0] + offset][line[1] - offset] += 1
        # left and up
        elif (line[0] > line[2]) and (line[1] > line[3]):
            for offset in range(line[0] - line[2] + 1):
                grid[line[0] - offset][line[1] - offset] += 1

countoverlaps(grid)