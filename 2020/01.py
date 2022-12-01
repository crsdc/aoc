# https://adventofcode.com/2020/day/1

with open('01data.txt', 'r') as datafile:
    input = list(map(int, datafile.readlines()))

# Part 1
for i in range(len(input)):
    for j in range(i + 1, len(input)):
        if input[i] + input[j] == 2020:
            print(input[i] * input[j])

# Part 2
for i in range(len(input)):
    for j in range(i + 1, len(input)):
        for k in range(j + 1, len(input)):
            if input[i] + input[j] + input[k] == 2020:
                print(input[i] * input[j] * input[k])