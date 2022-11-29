# https://adventofcode.com/2021/day/10

with open('10data.txt', 'r') as datafile:
    input = datafile.readlines()

stack = []
score1 = 0
score2list = []

for line in input:

    # Part 1: invalid lines
    for char in line.strip():
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            opener = stack.pop()
            if opener != '(' and char == ')':
                score1 += 3
            elif opener != '[' and char == ']':
                score1 += 57
            elif opener != '{' and char == '}':
                score1 += 1197
            elif opener != '<' and char == '>':
                score1 += 25137
            else:
                # Valid closure
                continue
            # After an invalid closure, move on to next line
            stack.clear()
            break

    # Part 2: incomplete lines
    score2 = 0
    while stack:
        score2 *= 5
        opener = stack.pop()
        if opener == '(':
            score2 += 1
        elif opener == '[':
            score2 += 2
        elif opener == '{':
            score2 += 3
        elif opener == '<':
            score2 += 4
    if score2 > 0:
        score2list.append(score2)

print(score1)
score2list.sort()
print(score2list[len(score2list) // 2])