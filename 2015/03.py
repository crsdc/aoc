# https://adventofcode.com/2015/day/3

with open("03data.txt", "r") as datafile:
    directions = datafile.readline()

# Part 1

x = 0
y = 0
visited = set()

for char in range(len(directions)):
    if directions[char] == '^':
        y -= 1
    elif directions[char] == 'v':
        y += 1
    elif directions[char] == '<':
        x -= 1
    elif directions[char] == '>':
        x += 1
    else:
        print('error')
    # Add position tuple to the set of visted positions
    visited.add((x, y))

print(len(visited))

# Part 2

santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0
visited2 = set()

for i in range(0, len(directions), 2):
    if directions[i] == '^':
        santa_y -= 1
    elif directions[i] == 'v':
        santa_y += 1
    elif directions[i] == '<':
        santa_x -= 1
    elif directions[i] == '>':
        santa_x += 1
    else:
        print('error')
    visited2.add((santa_x, santa_y))

    if directions[i + 1] == '^':
        robo_y -= 1
    elif directions[i + 1] == 'v':
        robo_y += 1
    elif directions[i + 1] == '<':
        robo_x -= 1
    elif directions[i + 1] == '>':
        robo_x += 1
    else:
        print('error')
    visited2.add((robo_x, robo_y))

print(len(visited2))