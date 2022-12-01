# https://adventofcode.com/2020/day/3

with open("03data.txt", "r") as datafile:
    lines = datafile.readlines()

data = []
for row in range(len(lines)):
    data.append(list(lines[row].strip()))

def checkslope(right, down):
    row = 0
    col = 0
    trees = 0

    while row < len(data):

        if col >= len(data[row]):
            col -= len(data[row])

        if data[row][col] == '#':
            trees += 1

        row += down
        col += right

    return trees

# Part 1

print(checkslope(3, 1))

# Part 2

print(checkslope(1, 1) * checkslope(3, 1) * checkslope(5, 1) * checkslope(7, 1) * checkslope(1, 2))