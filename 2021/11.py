# https://adventofcode.com/2021/day/11

energy = [[0 for i in range(10)] for j in range(10)]
with open('11data.txt', 'r') as datafile:
    for row, line in enumerate(datafile.readlines()):
        energy[row] = list(map(int,list(line.strip())))

flashcounter = 0
flashing = []
step = 0

def flashcheck(row, col):
    # Do nothing if trying to check a neighbour that's off the grid
    if row not in range(10) or col not in range(10):
        return
    # Do nothing if already established this location is flashing on this step
    if (row, col) in flashing:
        return
    # Increase energy but do nothing further if it doesn't trigger a flash
    energy[row][col] += 1
    if energy[row][col] <= 9:
        return
    # Keep track of how many flashes there have been
    global flashcounter
    flashcounter += 1
    # Now this location explored, follow up neighbours to see if they flash
    flashing.append((row, col))
    neighbours = [(row - 1, col),
                  (row + 1, col),
                  (row, col - 1),
                  (row, col + 1),
                  (row - 1, col - 1),
                  (row - 1, col + 1),
                  (row + 1, col - 1),
                  (row + 1, col + 1)]
    for octopus in neighbours:
        flashcheck(octopus[0], octopus[1])

while len(flashing) < 100:
    flashing.clear()
    step += 1
    # Go through grid incrementing energy and performing flashes
    for row in range(10):
        for col in range(10):
            flashcheck(row, col)
    # Reset energy level of all that flash on this step
    for octopus in flashing:
        energy[octopus[0]][octopus[1]] = 0
    # Part 1: how many total flashes after step 100?
    if step == 100:
        print(flashcounter)

# Part 2: how many steps in until all flash at once?
print(step)