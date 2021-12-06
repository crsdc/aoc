# https://adventofcode.com/2021/day/6

with open('06data.txt', 'r') as datafile:
    #fish = [3,4,3,1,2]
    fish = list(map(int, datafile.readline().split(',')))

# Part 1, naively giving individual fish their own list items

for day in range(1, 81):
    newfish = 0
    for i, timer in enumerate(fish):
        if timer > 0:
            fish[i] -= 1
        else:
            newfish += 1
            fish[i] = 6
    fish.extend([8] * newfish)

print(len(fish))

# Part 2, using a dictionary to keep track of how many fish have each timer value

fishcounts = dict.fromkeys([*range(9)])
for key in range(9):
    # Pick up already calculated values from day 80 rather than start again
    fishcounts[key] = fish.count(key)

for day in range(81, 257):
    # Note how many fish on 0 and move all fish down a day
    newfish = fishcounts[0]
    for key in range(8):
        fishcounts[key] = fishcounts[key + 1]
    # Add in the populations of new fish and reset fish previously on 0 to 6
    fishcounts[8] = newfish
    fishcounts[6] += newfish

print(sum(fishcounts.values()))