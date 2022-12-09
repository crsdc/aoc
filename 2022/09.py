# https://adventofcode.com/2022/day/9

def movehead(direction):
    if direction == 'U':
        head['y'] += 1
    elif direction == 'D':
        head['y'] -= 1
    elif direction == 'L':
        head['x'] -= 1
    elif direction == 'R':
        head['x'] += 1

def pulltailshort():
   tailrecord.add(moveknot(tail, head))

def pulltaillong():
    knotlist[0] = head
    for knot in range(1, 9):
        moveknot(knotlist[knot], knotlist[knot - 1])
    tailrecord.add(moveknot(knotlist[9], knotlist[8]))

def moveknot(knot, leader):
    if knot['x'] in range(leader['x'] - 1, leader['x'] + 2) and knot['y'] in range(leader['y'] - 1, leader['y'] + 2):
        return

    elif knot['x'] == leader['x'] - 2 and knot['y'] == leader['y']:
        knot['x'] += 1
    elif knot['x'] == leader['x'] + 2 and knot['y'] == leader['y']:
        knot['x'] -= 1
    elif knot['y'] == leader['y'] - 2 and knot['x'] == leader['x']:
        knot['y'] += 1
    elif knot['y'] == leader['y'] + 2 and knot['x'] == leader['x']:
        knot['y'] -= 1

    elif (knot['x'] == leader['x'] - 2 and knot['y'] == leader['y'] - 1) \
      or (knot['x'] == leader['x'] - 1 and knot['y'] == leader['y'] - 2):
        knot['x'] += 1
        knot['y'] += 1
    elif (knot['x'] == leader['x'] - 2 and knot['y'] == leader['y'] + 1) \
      or (knot['x'] == leader['x'] - 1 and knot['y'] == leader['y'] + 2):
        knot['x'] += 1
        knot['y'] -= 1
    elif (knot['x'] == leader['x'] + 2 and knot['y'] == leader['y'] - 1) \
      or (knot['x'] == leader['x'] + 1 and knot['y'] == leader['y'] - 2):
        knot['x'] -= 1
        knot['y'] += 1
    elif (knot['x'] == leader['x'] + 2 and knot['y'] == leader['y'] + 1) \
      or (knot['x'] == leader['x'] + 1 and knot['y'] == leader['y'] + 2):
        knot['x'] -= 1
        knot['y'] -= 1

    elif knot['x'] == leader['x'] - 2 and knot['y'] == leader['y'] - 2:
        knot['x'] += 1
        knot['y'] += 1
    elif knot['x'] == leader['x'] + 2 and knot['y'] == leader['y'] - 2:
        knot['x'] -= 1
        knot['y'] += 1
    elif knot['x'] == leader['x'] - 2 and knot['y'] == leader['y'] + 2:
        knot['x'] += 1
        knot['y'] -= 1
    elif knot['x'] == leader['x'] + 2 and knot['y'] == leader['y'] + 2:
        knot['x'] -= 1
        knot['y'] -= 1

    return((knot['x'], knot['y']))


with open('./09data.txt') as datafile:
    input = [line.strip().split() for line in datafile.readlines()]

# Part 1

head = {'x': 0, 'y': 0}
tail = {'x': 0, 'y': 0}
tailrecord = set()

for line in input:
    for _ in range(int(line[1])):
        movehead(line[0])
        pulltailshort()

print(len(tailrecord))

# Part 2

head = {'x': 0, 'y': 0}
knotlist = [{'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}]
tailrecord.clear()

for line in input:
    for _ in range(int(line[1])):
        movehead(line[0])
        pulltaillong()

print(len(tailrecord))