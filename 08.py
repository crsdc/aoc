# https://adventofcode.com/2021/day/8

def decode(pattern, config):
    # First check against digits that are obvious from their code length
    lengths = {1: 2, 4: 4, 7: 3, 8: 7}
    for digit, match in lengths.items():
        if len(pattern) == match:
            return digit
    # Failing that, check against the worked out configuration
    codes = {
        0: [config['A'], config['B'], config['C'], config['E'], config['F'], config['G']],
        2: [config['A'], config['C'], config['D'], config['E'], config['G']],
        3: [config['A'], config['C'], config['D'], config['F'], config['G']],
        5: [config['A'], config['B'], config['D'], config['F'], config['G']],
        6: [config['A'], config['B'], config['D'], config['E'], config['F'], config['G']],
        9: [config['A'], config['B'], config['C'], config['D'], config['F'], config['G']],
    }
    for digit, match in codes.items():
        if set(pattern) == set(match):
            return digit

data = []
with open('08data.txt', 'r') as datafile:
    for line in datafile.readlines():
        # Make each line a list where the output after the | is the last 4 items
        data.append(list(line.strip().replace(' | ', ' ').split()))

# Part 1

uniquesegments = 0
for line in data:
    for output in line[10:]:
        if len(output) in [2, 3, 4, 7]:
            uniquesegments += 1
print(uniquesegments)

# Part 2

total = 0
for line in data:
    config = {'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': ''}
    egposs, bdposs, cfposs = [], [], []

    # Find 1: must correspond to segments C and F, but can't say which is which
    for i, pattern in enumerate(line[:10]):
        if len(pattern) == 2:
            cfposs += pattern[0], pattern[1]
            break

    # Find 7: since we know which are C or F, other must be A
    for i, pattern in enumerate(line[:10]):
        if len(pattern) == 3:
            for letter in pattern:
                if letter not in cfposs:
                    config['A'] = letter
            break

    # Find 4: what isn't C or F must be B or D, but can't say which is which
    for i, pattern in enumerate(line[:10]):
        if len(pattern) == 4:
            for letter in pattern:
                if letter not in cfposs:
                    bdposs += letter
            break

    # Find 2,3,5: all have 5 segments
    for i, pattern in enumerate(line[:10]):
        if len(pattern) == 5:
            for letter in pattern:
                if letter not in cfposs + [config['A']] + bdposs:
                    egposs += letter
                if letter in bdposs:
                    bdposs += letter

    # Segment that 2,3,5 have in common that can't be A,B,C,D,F must be G
    # Segment only one digit (2) has that can't be A,B,C,D,F must be E
    egposs.sort()
    if egposs.count(egposs[0]) == 3:
        config['G'] = egposs[0]
        config['E'] = egposs[3]
    else:
        config['E'] = egposs[0]
        config['G'] = egposs[3]

    # Segment that 2,3,5 have in common that's one of B or D must be D
    bdposs.sort()
    if bdposs.count(bdposs[0]) == 4:
        config['D'] = bdposs[0]
        config['B'] = bdposs[5]
    else:
        config['B'] = bdposs[0]
        config['D'] = bdposs[5]

    # Find 0,6,9: all have 6 segments
    for i, pattern in enumerate(line[:10]):
        if len(pattern) == 6:
            for letter in pattern:
                if letter in cfposs:
                    cfposs += letter

    # Segment that 0,6,9 have in common that's one of C or F must be F
    cfposs.sort()
    if cfposs.count(cfposs[0]) == 4:
        config['F'] = cfposs[0]
        config['C'] = cfposs[6]
    else:
        config['C'] = cfposs[0]
        config['F'] = cfposs[6]

    total += decode(line[10], config) * 1000
    total += decode(line[11], config) * 100
    total += decode(line[12], config) * 10
    total += decode(line[13], config)

print(total)