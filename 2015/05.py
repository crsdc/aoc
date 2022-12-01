# https://adventofcode.com/2015/day/5

with open("05data.txt", "r") as datafile:
    input = list(map(lambda line: line.strip(), datafile.readlines()))

# Part 1

nicestrings = 0
vowels = 0

for line in input:

    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
        continue

    for char in line:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
    if vowels < 3:
        vowels = 0
        continue
    vowels = 0

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            nicestrings += 1
            break

print(nicestrings)

# Part 2

nicestrings = 0
pairtwice = False
splitrepeat = False

for line in input:

    for i in range(len(line) - 2):
        for j in range(i + 2, len(line) - 1):
            if line[i] == line[j] and line[i + 1] == line[j + 1]:
                pairtwice = True
                break

        if line[i] == line[i + 2]:
            splitrepeat = True

    if pairtwice and splitrepeat:
        nicestrings += 1
    pairtwice = False
    splitrepeat = False

print(nicestrings)