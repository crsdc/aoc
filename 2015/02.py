# https://adventofcode.com/2015/day/2

with open("02data.txt", "r") as datafile:
    lines = datafile.readlines()

# Read lines into long list consisting of lists of 3 elements
dimensions = [[0, 0, 0] for i in range(len(lines))]
for box, line in enumerate(lines):
    dimensions[box] = list(map(int, line.split('x')))

area = 0
ribbon = 0

for box in range(len(dimensions)):

    # Sort dimensions to identify smallest side
    dimensions[box].sort()

    # Extra side's worth of area for the smallest side
    area += 3 * dimensions[box][0] * dimensions[box][1]
    area += 2 * dimensions[box][1] * dimensions[box][2]
    area += 2 * dimensions[box][0] * dimensions[box][2]

    # Ribbon is smallest perimeter plus a number equal to the volume
    ribbon += 2 * dimensions[box][0] + 2 * dimensions[box][1]
    ribbon += dimensions[box][0] * dimensions[box][1] * dimensions[box][2]

print(area)
print(ribbon)
