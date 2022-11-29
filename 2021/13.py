# https://adventofcode.com/2021/day/13

points = set()
folds = []

with open('13data.txt', 'r') as datafile:
    for line in datafile.readlines():
        # Store point coords in a set of tuples of form (x, y)
        if ',' in line:
            points.add(tuple(map(int, line.strip().split(','))))
        # Store folds in a list of tuples of form ('y', 100)
        elif '=' in line:
            fold = line.strip().replace('fold along ','').split('=')
            folds.append( (fold[0], int(fold[1])) )

for i, fold in enumerate(folds):
    newpoints = set()
    if fold[0] == 'x':
        for point in points:
            if point[0] > fold[1]:
                # Point is to the right of the fold, so perform reflection
                reflected = (fold[1] - (point[0] - fold[1]), point[1])
                newpoints.add(reflected)
            else:
                # Points to the left of the fold are carried over unaffected
                newpoints.add(point)
    else:
        # fold[0] == 'y' so reflect if point is below the fold
        for point in points:
            if point[1] > fold[1]:
                reflected = (point[0], fold[1] - (point[1] - fold[1]))
                newpoints.add(reflected)
            else:
                newpoints.add(point)

    # Replace set with transformed one
    points = newpoints

    # Part 1: print how many points in the set after 1 fold
    if i == 0:
        print(len(points))


# Part 2: display grid with points after all folds

# Cut corner by inspecting data, but could replace with code to find dimensions
ymax, xmax = 6, 39
grid = [[' ' for y in range(ymax)] for x in range(xmax)]

for point in points:
    # Unicode solid block for readability
    grid[point[0]][point[1]] = '\u2588'

for y in range(ymax):
    for x in range(xmax):
        print(grid[x][y], end='')
    print()