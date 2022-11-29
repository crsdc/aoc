# https://adventofcode.com/2021/day/2

with open("02data.txt", "r") as datafile:
    commandlist = datafile.readlines()

# Part 1

horizontal = 0
depth = 0

for n in commandlist:
    command = n.strip().split(' ')
    if (command[0] == "forward"):
        horizontal += int(command[1])
    elif (command[0] == "down"):
        depth += int(command[1])
    elif (command[0] == "up"):
        depth -= int(command[1])

print ("H   ", horizontal)
print ("D   ", depth)
print ("HxD ", horizontal * depth)

# Part 2

horizontal = 0
depth = 0
aim = 0

for n in commandlist:
    command = n.strip().split(' ')
    if (command[0] == "forward"):
        horizontal += int(command[1])
        depth += aim * int(command[1])
    elif (command[0] == "down"):
        aim += int(command[1])
    elif (command[0] == "up"):
        aim -= int(command[1])

print ("")
print ("A   ", aim)
print ("H   ", horizontal)
print ("D   ", depth)
print ("HxD ", horizontal * depth)