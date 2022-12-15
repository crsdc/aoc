# https://adventofcode.com/2022/day/15
# untidy version, one star

import re, sys

#with open('./testdata.txt') as datafile:
with open('./15data.txt') as datafile:
    input = datafile.readlines()

pairs = []
for line in input:
    pairs.append([int(num) for num in re.split(', y=|: closest beacon is at x=', line.strip()[12:])])

for pair in pairs:
    # Calculate Manhattan distance
    pair.append(abs(pair[0] - pair[2]) + abs(pair[1] - pair[3]))
    #print(pair)

#tline = 10
tline = 2000000
overlap = set()
for pair in pairs:
    # Does row intersect the area covered by sensor?
    if abs(tline - pair[1]) <= pair[4]:
        # How many points on row are within Manhattan distance of sensor?
        intersectionlength = 1 + 2 * (pair[4] - abs(tline - pair[1]))
        #print(intersectionlength)
        # Record points left and right of closest intersection
        covered = [x for x in range(pair[0] - intersectionlength // 2, pair[0] + intersectionlength // 2 + 1)]
        #print(covered)
        overlap.update(covered)

#print(overlap, len(overlap))

linebeacons = set()
for pair in pairs:
    if pair[2] in overlap and pair[3] == tline:
        linebeacons.add(pair[2])

print(len(overlap) - len(linebeacons))

coverage = []
#for y in range(21):
for y in range(4000001):
    #print(y)
    coverage.append([])

for pair in pairs:
    print('ooo', pair)
    if pair[1] - pair[4] >= 0:
        ystart = pair[1] - pair[4]
    else:
        ystart = 0
    if pair[1] + pair[4] <= 20:
        yfinish = pair[1] + pair[4]
    else:
        #yfinish = 20
        yfinish = 4000000
    for y in range(ystart, yfinish + 1):
        xstart = pair[0] - (pair[4] - abs(y - pair[1]))
        xfinish = pair[0] + (pair[4] - abs(y - pair[1]))
        #print(y, xstart, xfinish)

        if xstart < 0:
            xstart = 0
        #if xfinish > 20:
        #    xfinish = 20
        if xfinish > 4000000:
            xfinish = 4000000

        #check for overlap
        if len(coverage[y]) == 0:
            coverage[y] += [xstart, xfinish]
        else:
            added = False
            for i in range(1, len(coverage[y]), 2):
                if xstart < coverage[y][i - 1] and xfinish > coverage[y][i]:
                    coverage[y][i - 1] = xstart
                    coverage[y][i] = xfinish
                    break
                elif xstart >= coverage[y][i - 1] and xfinish <= coverage[y][i]:
                    continue
                elif xfinish < coverage[y][i - 1]:
                    coverage[y] += [xstart, xfinish]
                    break
                elif xstart > coverage[y][i]:
                    coverage[y] += [xstart, xfinish]
                    break
                elif xstart < coverage[y][i - 1] and xfinish in range(coverage[y][i - 1], coverage[y][i] + 1):
                    coverage[y][i - 1] = xstart
                    break
                elif xfinish > coverage[y][i] and xstart in range(coverage[y][i - 1], coverage[y][i] + 1):
                    coverage[y][i] = xfinish
                    break
                else:
                    print('argggg!!!!!!!!!!!', xstart, xfinish, coverage[y][i-1], coverage[y][i])
            if not added:
                coverage[y] += [xstart, xfinish]


        #print(coverage[y])


print('...........')
for y, row in enumerate(coverage):
    print(y)
    #print(y, row)
    #for x in range(21):
    for x in range(4000001):
        able = True
        for bound in range(1, len(coverage[y]) + 1, 2):
            if x in range(coverage[y][bound - 1], coverage[y][bound] + 1):
                able = False
                break
        if able:
            print(x, y, 'ABLE', x * 4000000 + y)
            sys.exit()