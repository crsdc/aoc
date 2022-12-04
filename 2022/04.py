# https://adventofcode.com/2022/day/4

import re

with open('./04data.txt') as datafile:
    input = datafile.readlines()

fullycontained = 0
overlap = 0

for line in input:
    pairs = [int(bound) for bound in re.split(',|-', line.strip())]
    set1 = set(range(pairs[0], pairs[1] + 1))
    set2 = set(range(pairs[2], pairs[3] + 1))
    if set1.issubset(set2) or set1.issuperset(set2):
        fullycontained += 1
    if not set1.isdisjoint(set2):
        overlap += 1

print(fullycontained)
print(overlap)