# https://adventofcode.com/2015/day/1

with open("01data.txt", "r") as datafile:
    instructions = datafile.readline()

floor = 0
basementalready = False

for char in range(len(instructions)):
    if instructions[char] == '(':
        floor += 1
    elif instructions[char] == ')':
        floor -= 1
    else:
        print('Unexpected character')

    if floor < 0 and basementalready == False:
        print('Entered basement at character:', char + 1)
        basementalready = True

print('Final floor:', floor)