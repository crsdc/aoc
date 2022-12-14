# https://adventofcode.com/2022/day/14

def fallfrom(x, y, part):
    # Test for abyss in part 1
    if part == 1 and y >= limB:
        return False

    # Position is in range so see if grain can fall further
    if grid[x][y + 1] == '.':
        result = fallfrom(x, y + 1, part) # down
    elif grid[x - 1][y + 1] == '.':
        result = fallfrom(x - 1, y + 1, part) # down and left
    elif grid[x + 1][y + 1] == '.':
        result = fallfrom(x + 1, y + 1, part) # down and right
    else:
        # Grain can't fall any further but can be placed successfully
        grid[x][y] = 'o'
        result = True

    # Pass result back up through the recursion
    return result


with open('./14data.txt') as datafile:
    input = datafile.readlines()

limB = 166

# Draw blank grid
grid = []
for x in range(1000):
    xline = []
    for y in range(0, limB + 1):
        xline += '.'
    grid.append(xline)

for line in input:
    # Parse input
    pointstrings = line.strip().split(' -> ')
    points = []
    for point in pointstrings:
        x, y = point.split(',')
        points.append([int(x), int(y)])

    # Draw lines
    for i in range(1, len(points)):
        x1, y1, x2, y2 = points[i - 1][0], points[i - 1][1], points[i][0], points[i][1]
        if x1 == x2:
            # Vertical line
            if y1 < y2:
                for y in range(y1, y2 + 1):
                    grid[x1][y] = '#'
            elif y2 < y1:
                for y in range(y2, y1 + 1):
                    grid[x1][y] = '#'
        elif y1 == y2:
            # Horizontal line
            if x1 < x2:
                for x in range(x1, x2 + 1):
                    grid[x][y1] = '#'
            elif x2 < x1:
                for x in range(x2, x1 + 1):
                    grid[x][y1] = '#'

# Part 1

# Drop sand until some falls into abyss
sandcount = 0
while True:
    result = fallfrom(500, 0, 1)
    if result is True:
        sandcount += 1
    else:
        print(sandcount)
        break

# Part 2

# Add the floor underneath all the way along
for x in grid:
    x += ('.', '#')

# Keep dropping sand until it piles up to the source
while grid[500][0] == '.':
    fallfrom(500, 0, 2)
    sandcount +=1

print(sandcount)