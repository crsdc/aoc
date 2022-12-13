# https://adventofcode.com/2022/day/13

def parse(start, data):
    parsed = []
    depth = 0
    numstring = ''

    for i in range(start, len(data)):
        if depth == 1:
            if data[i] == '[':
                parsed.append(parse(i, data))
            elif data[i] == ',':
                if numstring != '':
                    parsed.append(int(numstring))
                numstring = ''
            elif data[i] == ']':
                if numstring != '':
                    parsed.append(int(numstring))
                return parsed
            else:
                numstring += data[i]

        if data[i] == '[':
            depth += 1
        elif data[i] == ']':
            depth -= 1


def compare(pair):
    for i in range(len(pair[0])):
        if len(pair[1]) < i + 1:
            # Right ran out before left
            return False

        if type(pair[0][i]) is int and type(pair[1][i]) is int:
            if pair[0][i] < pair[1][i]:
                return True
            elif pair[0][i] > pair[1][i]:
                return False
        elif type(pair[0][i]) is list and type(pair[1][i]) is list:
            comparison = compare([pair[0][i], pair[1][i]])
            if comparison is True or comparison is False:
                return comparison
        elif type(pair[0][i]) is int and type(pair[1][i]) is list:
            # Convert left int to list and compare lists
            comparison = compare([[pair[0][i]], pair[1][i]])
            if comparison is True or comparison is False:
                return comparison
        elif type(pair[0][i]) is list and type(pair[1][i]) is int:
            # Convert right int to list and compare lists
            comparison = compare([pair[0][i], [pair[1][i]]])
            if comparison is True or comparison is False:
                return comparison

    if len(pair[0]) < len(pair[1]):
        # Left ran out before right
        return True


with open('./13data.txt') as datafile:
    input = datafile.readlines()

pairs = []
for i in range(len(input) // 3 + 1):
    pairs.append([parse(0, input[i * 3].strip()), parse(0, input[i * 3 + 1].strip())])

# Part 1

sum = 0
for index, pair in enumerate(pairs):
    if compare(pair):
        sum += index + 1

print(sum)

# Part 2

packets = []
packets += [[[2]], [[6]]]

for line in input:
    if line != '\n':
        packets.append(parse(0, line.strip()))

# Bubble sort to keep things simple
done = False
while not done:
    done = True
    for i in range(1, len(packets)):
        if compare([packets[i - 1], packets[i]]) is False:
            temp = packets[i]
            packets[i] = packets[i - 1]
            packets[i - 1] = temp
            done = False

dividerpositions = []
for i, packet in enumerate(packets):
    if packet == [[2]] or packet == [[6]]:
        dividerpositions.append(i + 1)

print(dividerpositions[0] * dividerpositions[1])