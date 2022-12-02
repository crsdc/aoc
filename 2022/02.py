# https://adventofcode.com/2022/day/2

with open("02data.txt", "r") as datafile:
    input = datafile.readlines()

data = []
for line in input:
    data.append(line.split())

# Part 1

choicescore = {
    'X': 1, # rock
    'Y': 2, # paper
    'Z': 3, # scissors
}

def outcomescore(player, opponent):
    if (player == 'X' and opponent == 'A') \
    or (player == 'Y' and opponent == 'B') \
    or (player == 'Z' and opponent == 'C'):
        return 3 # draw
    elif (player == 'X' and opponent == 'C') \
      or (player == 'Y' and opponent == 'A') \
      or (player == 'Z' and opponent == 'B'):
        return 6 # player wins
    else:
        return 0 # player loses

score = 0
for round in data:
    score += choicescore.get(round[1])
    score += outcomescore(round[1], round[0])

print(score)

# Part 2

choicescore2 = {
    'A': 1, # rock
    'B': 2, # paper
    'C': 3, # scissors
}

pairwise = {
    'A': 'C', # rock beats scissors
    'B': 'A', # paper beats rock
    'C': 'B', # scissors beat paper
}

def fixround(outcome, opponent):
    if outcome == 'X': # lose
        return choicescore2[ pairwise[opponent] ]
    elif outcome == 'Y': # draw
        return choicescore2[opponent] + 3
    else: # 'Z' win - look up dict key by value
        for item in pairwise.items():
            if item[1] == opponent:
                return choicescore2[ item[0] ] + 6

score = 0
for round in data:
    score += fixround(round[1], round[0])

print(score)