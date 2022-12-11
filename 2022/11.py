# https://adventofcode.com/2022/day/11

with open('./11data.txt') as datafile:
    input = datafile.readlines()

def parseinput():
    monkeys = []
    for line in input:
        if line[:6] == 'Monkey':
            monkeys.append({'inspections': 0})
        if line[:16] == '  Starting items':
            monkeys[-1]['items'] = [int(item.strip(',')) for item in line.split()[2:]]
        if line[:11] == '  Operation':
            if line.strip()[-9:] == 'old * old':
                monkeys[-1]['operation'] = 'square'
            else:
                monkeys[-1]['operation'] = line.strip().split()[-2]
                monkeys[-1]['operand'] = int(line.strip().split()[-1])
        if line[:6] == '  Test':
            monkeys[-1]['divisor'] = int(line.strip().split()[-1])
        if line[:11] == '    If true':
            monkeys[-1]['iftrue'] = int(line.strip().split()[-1])
        if line[:12] == '    If false':
            monkeys[-1]['iffalse'] = int(line.strip().split()[-1])
    return monkeys

def playround(part):
    for monkey in monkeys:
        for score in monkey['items']:
            monkey['items'] = monkey['items'][1:]
            monkey['inspections'] += 1

            if monkey['operation'] == '+':
                score += monkey['operand']
            elif monkey['operation'] == '*':
                score *= monkey['operand']
            else: # square
                score *= score

            if part == 1:
                score //= 3
            elif part == 2:
                score %= commonfactor

            if score % monkey['divisor'] == 0:
                monkeys[monkey['iftrue']]['items'].append(score)
            else:
                monkeys[monkey['iffalse']]['items'].append(score)

def getresult():
    inspectioncounts = sorted([monkey['inspections'] for monkey in monkeys])
    print(inspectioncounts[-1] * inspectioncounts[-2])

# Part 1

monkeys = parseinput()

for round in range(20):
    playround(1)

getresult()

# Part 2

monkeys = parseinput()

factorlist = [monkey['divisor'] for monkey in monkeys]
commonfactor = 1
for factor in factorlist:
    commonfactor *= factor

for round in range(10000):
    playround(2)

getresult()