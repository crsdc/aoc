# https://adventofcode.com/2022/day/12
# horribly untidy version, one star so far!

import sys


def explorefrom(pos):
    global visited, firstdist
    #visited.append(pos)
    x = pos['x']
    y = pos['y']
    if x == destination['x'] and y == destination['y']:
        print('dest', grid[y][x]['dis'])
        firstdist = grid[y][x]['dis']
        return
        sys.exit()
        return
    distance = grid[y][x]['dis']
    elev = grid[y][x]['elv']
    print('x',x,'y',y,'dist',distance,'e',elev)
    if distance == 200:
        sys.exit()

    neighbs = {'d': -1, 'l': -1, 'r': -1, 'u': -1}
    if y < ylen - 1:
        neighbs['d'] = checkpos({'y': y + 1, 'x': x}, elev, distance)
    if x > 0:
        neighbs['l'] = checkpos({'y': y, 'x': x-1}, elev, distance)
    if x < xlen - 1:
        neighbs['r'] = checkpos({'y': y, 'x': x+1}, elev, distance)
    if y > 0:
        neighbs['u'] = checkpos({'y': y - 1, 'x': x}, elev, distance)
    neighbsort = sorted(neighbs.items(), key=lambda x:x[1])
    print(neighbsort)
    if neighbsort[0][0] == 'd':
        explorefrom({'y': y+1, 'x': x})
    elif neighbsort[0][0] == 'l':
        explorefrom({'y': y, 'x': x-1})
    elif neighbsort[0][0] == 'r':
        explorefrom({'y': y, 'x': x+1})
    elif neighbsort[0][0] == 'u':
        explorefrom({'y': y-1, 'x': x})


def checkpos(pos, elev, distance):
    x = pos['x']
    y = pos['y']
    if grid[y][x]['elv'] <= elev + 1 and {'x': x, 'y': y} not in visited:
        if grid[y][x]['dis'] > distance + 1 or grid[y][x]['dis'] == -1:
            grid[y][x]['dis'] = distance + 1
            print(x, y, grid[y][x]['elv'])
            return grid[y][x]['dis']
    return -1



with open('./testdata.txt', 'r') as datafile:
#with open('./12data.txt') as datafile:
    input = datafile.readlines()

grid = []
start = {}
destination = {}
ylen = len(input)
xlen = len(input[0]) -1
visited = []
queue = []

for y, line in enumerate(input):
    row = []
    for x, char in enumerate(line.strip()):
        if char == 'S':
            start = {'x': x, 'y': y}
            row.append({'elv': 1, 'dis': 0}) # tuple of letter value, distance
            #visited += start
        elif char == 'E':
            destination = {'x': x, 'y': y}
            row.append({'elv': 26, 'dis': -1}) # -1 to signify unknown distance
        else:
            row.append({'elv': ord(char) - 96, 'dis': -1})
    grid.append(row)

#print(grid)

#print(destination)



def explor(pos):
    global queue
    x = pos['x']
    y = pos['y']
    distance = grid[y][x]['dis']
    elev = grid[y][x]['elv']

    #print('at', x, y, elev, distance)


    if pos == destination:
        print('dest', distance)
        #sys.exit()
        return

    adjacent = []
    if y < ylen - 1:
        adjacent.append({'y': y + 1, 'x': x})
    if x > 0:
        adjacent.append({'y': y, 'x': x - 1})
    if x < xlen - 1:
        adjacent.append({'y': y, 'x': x + 1})
    if y > 0:
        adjacent.append({'y': y - 1, 'x': x})

    for neighb in adjacent:
        if grid[neighb['y']][neighb['x']]['elv'] <= elev + 1 and {'x': x, 'y': y} not in visited:
            grid[neighb['y']][neighb['x']]['dis'] = distance + 1
            #print('neighb', neighb['x'], neighb['y'], grid[neighb['y']][neighb['x']]['elv'], grid[neighb['y']][neighb['x']]['dis'])
            queue.append(neighb)

    visited.append(pos)

    return


            #if grid[neighb['y']][neighb['x']]['dis'] > distance + 1 or grid[neighb['y']][neighb['x']]['dis'] == -1:
            #    grid[neighb['y']][neighb['x']]['dis'] = distance + 1

firstdist = 0

queue.append(start)

pos = start

while len(queue) > 0:
    explor(queue[0])
    queue = queue[1:]


lowest = firstdist

#optionlist = []
for y, col in enumerate(grid):
    for x, option in enumerate(col):
        if option['elv'] == 1 and option['dis'] != -1:
            print(x, y, option['dis'])
            #optionlist.append({'x': x, 'y': y})
#print(optionlist)
#print(len(optionlist))

print(lowest)

#for option in optionlist:
#    print(option)
#    queue.clear()
#    visited.clear()

#    for y, col in enumerate(grid):
#        for x, row in enumerate(col):
#            grid[y][x]['dis'] = -1
    #print(option['y'])
    #print(option['x'])
#    grid[option['y']][option['x']]['dis'] = 0

#    queue.append(option)
#    while len(queue) > 0:
#        explor(queue[0])
#        queue = queue[1:]




#print(visited)
#print(grid)

