# https://adventofcode.com/2022/day/8

def isvisible(xtree, ytree, height):
    blocked = False
    for x in range(0, xtree):
        if input[ytree][x] >= height:
            blocked = True
            break
    if not blocked:
        return True
    blocked = False
    for x in range(xtree + 1, xlen):
        if input[ytree][x] >= height:
            blocked = True
            break
    if not blocked:
        return True
    blocked = False
    for y in range(0, ytree):
        if input[y][xtree] >= height:
            blocked = True
            break
    if not blocked:
        return True
    blocked = False
    for y in range(ytree + 1, ylen):
        if input[y][xtree] >= height:
            blocked = True
            break
    if not blocked:
        return True
    return False

def scenic(xtree, ytree, height):
    distanceE = 0
    for x in range(xtree + 1, xlen):
        distanceE += 1
        if input[ytree][x] >= height:
            break
    distanceW = 0
    for x in range(xtree - 1, -1, -1):
        distanceW += 1
        if input[ytree][x] >= height:
            break
    distanceS = 0
    for y in range(ytree + 1, ylen):
        distanceS += 1
        if input[y][xtree] >= height:
            break
    distanceN = 0
    for y in range(ytree - 1, -1, -1):
        distanceN += 1
        if input[y][xtree] >= height:
            break
    return distanceE * distanceW * distanceS * distanceN

with open('./08data.txt') as datafile:
    input = [line.strip() for line in datafile.readlines()]

xlen = len(input[0])
ylen = len(input)

# Part 1
visible = 0
for y, line in enumerate(input):
    for x, height in enumerate(line):
        if x == 0 or x == xlen - 1 or y == 0 or y == ylen - 1:
            visible += 1
        elif isvisible(x, y, height):
            visible += 1
print(visible)

# Part 2
highscore = 0
for y, line in enumerate(input):
    for x, height in enumerate(line):
        newscore = scenic(x, y, height)
        if newscore > highscore:
            highscore = newscore
print(highscore)