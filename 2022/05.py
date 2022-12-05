# https://adventofcode.com/2022/day/5

def initmoves(input):
    moves = []
    for line in input:
        if line[0] == 'm':
            move = line.strip().split()
            moves.append([int(number) for number in [move[1], move[3], move[5]]])
    return moves

def initstacks(input):
    stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for line in input:
        if line[0] == '[':
            for i in range(1, len(line), 4):
                if line[i] != ' ':
                    stacks[i // 4 + 1].append(line[i])
    for stack in stacks:
        stacks[stack].reverse()
    return stacks

def topcrates(stacks):
    topcrates=''
    for key in stacks:
        topcrates += stacks[key].pop()
    return topcrates

def rearrange1(stacks, moves):
    for move in moves:
        for i in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())
    return topcrates(stacks)

def rearrange2(stacks, moves):
    for move in moves:
        chunk = stacks[move[1]][-(move[0]):]
        del stacks[move[1]][-(move[0]):]
        stacks[move[2]] += chunk
    return topcrates(stacks)

with open('./05data.txt') as datafile:
    input = datafile.readlines()

moves = initmoves(input)
stacks = initstacks(input)
print(rearrange1(stacks, moves))
stacks = initstacks(input)
print(rearrange2(stacks, moves))