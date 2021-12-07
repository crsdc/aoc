# https://adventofcode.com/2021/day/7

with open('07data.txt', 'r') as datafile:
    #positions = [16,1,2,0,4,2,7,1,2,14]
    positions = list(map(int, datafile.readline().split(',')))

# Part 1

positions.sort()
median = positions[ int(len(positions) / 2) ]

fuel = 0
for i in positions:
    fuel += abs(i - median)

print(fuel)

# Part 2

nearmean = round(sum(positions) / len(positions)) - 1

fuel = 0
for i in positions:
    fuel += abs(i - nearmean) * (abs(i - nearmean) + 1) / 2

print(int(fuel))
