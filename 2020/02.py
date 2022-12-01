# https://adventofcode.com/2020/day/2

import re

with open('02data.txt', 'r') as datafile:
    input = datafile.readlines()

data = []
for line in input:
    data.append(re.split('-| |: ', line.strip()))

# Part 1

validcount = 0
for line in data:
    occurrences = list(line[3]).count(line[2])
    if occurrences >= int(line[0]) and occurrences <= int(line[1]):
        validcount += 1

print(validcount)

# Part 2

validcount = 0
for line in data:
    if list(line[3])[int(line[0]) - 1] == line[2]:
        if list(line[3])[int(line[1]) - 1] != line[2]:
            validcount += 1
    elif list(line[3])[int(line[1]) - 1] == line[2]:
        validcount += 1

print(validcount)