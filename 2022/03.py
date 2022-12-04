# https://adventofcode.com/2022/day/3

with open('./03data.txt') as datafile:
    input = datafile.readlines()

def priorityvalue(char):
    if ord(char) in range(65, 92):
        # upper case, ASCII values 65-91, need 27-52
        return ord(char) - 38
    else:
        # lower case, ASCII values 97-122, need 1-26
        return ord(char) - 96

def findduplicate(line):
    halfway = len(line) // 2
    for char in line[:halfway]:
        for char2 in line[halfway:]:
            if char == char2:
                return priorityvalue(char)

def findbadge(line):
    for char in input[line]:
        for char2 in input[line + 1]:
            if char == char2:
                for char3 in input[line + 2]:
                    if char == char3:
                        return priorityvalue(char)

prioritysum = 0
for line in input:
    prioritysum += findduplicate(line)
print(prioritysum)

prioritysum = 0
for line in range(0, len(input), 3):
    prioritysum += findbadge(line)
print(prioritysum)