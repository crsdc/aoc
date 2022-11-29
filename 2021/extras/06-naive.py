# https://adventofcode.com/2021/day/6
# Naive method to solve part 1 extended to part 2, where it becomes infeasible

from sys import getsizeof

with open('../06data.txt', 'r') as datafile:
    #fish = [3,4,3,1,2]
    fish = list(map(int, datafile.readline().split(',')))

for day in range(1, 257):
    newfish = 0
    for i, timer in enumerate(fish):
        if timer > 0:
            fish[i] -= 1
        else:
            newfish += 1
            fish[i] = 6
    fish.extend([8] * newfish)
    print(getsizeof(fish), "bytes for", len(fish), "at end of day", day)
