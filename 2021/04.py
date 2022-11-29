# https://adventofcode.com/2021/day/4

# function to add up winning scores
winlist = list()
def winboard(board, called):
    scoresum = 0
    # first check whether board already won
    if board in winlist:
        return
    winlist.append(board)
    # scan winning table for unmarked numbers
    for row in range(5):
        for col in range(5):
            if numbers[board][row][col].marked == False:
                scoresum += numbers[board][row][col].value
    print('Board', board, 'wins with score', scoresum * called)

# read in the file and the sequence of called numbers
with open('04data.txt', 'r') as datafile:
    inputlist = datafile.readlines()
sequence = inputlist[0].split(',')

# each number in the tables has an integer value and a bool for whether marked
class Number:
    def __init__(self):
        self.value = 0
        self.marked = False

# read tables into array of Numbers organised as numbers[board][row][col]
numbers = [[[Number() for i in range(5)] for j in range(5)] for k in range(100)]
board = 0
row = 0
for line in range(2, len(inputlist)):
    # check for blank lines and move on to the next table
    if inputlist[line] == '\n':
        board += 1
        row = 0
        continue
    # get the 5 numbers from each table line and put them in the array
    for col in range(5):
        numbers[board][row][col].value = int(inputlist[line].split()[col])
    row += 1

# step through the sequence calling and marking numbers
for called in sequence:
    # search the array and mark matched numbers
    for board in range(100):
        for row in range(5):
            for col in range(5):
                if int(called) == numbers[board][row][col].value:
                    numbers[board][row][col].marked = True
    # check each board for a winner
    for board in range(100):
        # check for winning rows
        for row in range(5):
            for col in range(5):
                if numbers[board][row][col].marked == False:
                    break
            else:
                winboard(board, int(called))
        # check for winning columns
        for col in range(5):
            for row in range(5):
                if numbers[board][row][col].marked == False:
                    break
            else:
                winboard(board, int(called))