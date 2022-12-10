# https://adventofcode.com/2022/day/10

def cycle():
    global clock, sum
    if x in range(clock % 40 - 1, clock % 40 + 2):
        print('#', end='')
    else:
        print('.', end='')
    if clock % 40 == 39:
        print('')
    clock += 1
    if clock % 40 == 20:
        sigstrength = clock * x
        sum += sigstrength

with open('./10data.txt') as datafile:
    input = [line.strip().split() for line in datafile.readlines()]

clock = 0
x = 1
sum = 0

for line in input:
    if line[0] == 'addx':
        cycle()
        cycle()
        x += int(line[1])
    elif line[0] == 'noop':
        cycle()

print(sum)