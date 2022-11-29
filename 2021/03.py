# https://adventofcode.com/2021/day/3

with open('03data.txt', 'r') as datafile:
    inputlist = datafile.readlines()

# Part 1

counter = [0] * 12
gamma = ''
epsilon = ''

for line in inputlist:
    for i in range(len(line) - 1):
        if (line[i] == '1'):
            counter[i] += 1

for count in counter:
    if (count > len(inputlist) / 2):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print (int(gamma, 2) * int(epsilon, 2))

# Part 2

# oxygen
counter = [0] * 12
oxygen = 0

# take a copy of the list so the original is available for co2
trimlist = inputlist.copy()

# look at each bit position in turn
for bit in range(12):

    # scan the list
    for line in trimlist:
        # if the relevant bit in the line is 1 increment counter
        if (line[bit] == '1'):
            counter[bit] += 1

    # see if half or more of the list had 1 for the relevant bit
    if (counter[bit] >= len(trimlist) / 2):
        # blank out all list items that have a 0 here
        for line in range(len(trimlist)):
            if (trimlist[line][bit] == '0'):
                trimlist[line] = ""
    # or if more than half the list had 0 blank out lines with 1 instead
    else:
        for line in range(len(trimlist)):
            if (trimlist[line][bit] == '1'):
                trimlist[line] = ""

    # trim the list by filtering out all the blank lines
    trimlist = list(filter(None, trimlist))

    # check if list is down to 1 item
    if (len(trimlist) == 1):
        oxygen = int(trimlist[0], 2)
        print(oxygen)
        break

# co2
counter = [0] * 12
co2 = 0

for bit in range(12):

    for line in inputlist:
        if (line[bit] == '1'):
            counter[bit] += 1

    if (counter[bit] >= len(inputlist) / 2):
        for line in range(len(inputlist)):
            if (inputlist[line][bit] == '1'):
                inputlist[line] = ""
    else:
        for line in range(len(inputlist)):
            if (inputlist[line][bit] == '0'):
                inputlist[line] = ""
                
    inputlist = list(filter(None, inputlist))
    
    if (len(inputlist) == 1):
        co2 = int(inputlist[0], 2)
        print(co2)
        break

print(oxygen * co2)