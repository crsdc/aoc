# https://adventofcode.com/2021/day/9

grid = [[0 for i in range(100)] for j in range(100)]
with open('09data.txt', 'r') as datafile:
    for row, line in enumerate(datafile.readlines()):
        grid[row] = list(map(int,list(line.strip())))

# Part 1

risksum = 0
minima = []

for row in range(100):
    for col in range (100):
        # Check neighbour to see if it's lower
        if row in range(1, 100):
            if grid[row - 1][col] <= grid[row][col]:
                continue
        if row in range(0, 99):
            if grid[row + 1][col] <= grid[row][col]:
                continue
        if col in range(1, 100):
            if grid[row][col - 1] <= grid[row][col]:
                continue
        if col in range(0, 99):
            if grid[row][col + 1] <= grid[row][col]:
                continue
        # If got to here, this location is a low point so add its risk score
        risksum += grid[row][col] + 1
        # Keep a note of location in a list of tuples for part 2
        minima.append((row, col))

print(risksum)

# Part 2

def checkaround(location):
    # This location must be part of a basin, so add it to the list
    basin.append(location)
    row, col = location[0], location[1]
    # Check each neighbour to see if it's on the edge, a 9, or already known
    # If none of those, check its neighbours to keep exploring the basin
    if row in range(1, 100):
        if grid[row - 1][col] != 9 and (row - 1, col) not in basin:
            checkaround((row - 1, col))
    if row in range(0, 99):
        if grid[row + 1][col] != 9 and (row + 1, col) not in basin:
            checkaround((row + 1, col))
    if col in range(1, 100):
        if grid[row][col - 1] != 9 and (row, col - 1) not in basin:
            checkaround((row, col - 1))
    if col in range(0, 99):
        if grid[row][col + 1] != 9 and (row, col + 1) not in basin:
            checkaround((row, col + 1))

basinsizes = []

# Start a recursion from each known low point
for location in minima:
    basin = []
    checkaround(location)
    # Once out of a recursion, log how many locations were in basin
    basinsizes.append(len(basin))

# Use the size of the three largest basins
basinsizes.sort()
print(basinsizes[len(basinsizes) - 3] * basinsizes[len(basinsizes) - 2] * basinsizes[len(basinsizes) - 1])