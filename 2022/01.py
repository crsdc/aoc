# https://adventofcode.com/2022/day/1

with open("01data.txt", "r") as datafile:
    lines = datafile.readlines()

elves = []
i = 0
for line in lines:
    if line == '\n':
        i += 1
    else:
        if len(elves) == i:
            elves.append(int(line))
        else:
            elves[i] += int(line)

# Part 1
print(max(elves))

# Part 2
elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])