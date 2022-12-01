# https://adventofcode.com/2020/day/4

with open("04data.txt", "r") as datafile:
    lines = datafile.readlines()

data = []

index = 0
for line in lines:
    if line == '\n':
        index += 1
        continue
    else:
        # records are sometimes split over multiple lines
        if len(data) == index:
            data.append(line.strip().split())
        else:
            data[index] += line.strip().split()

# Part 1

validcount = 0
for record in data:

    if len(record) < 7:
        continue

    elif len(record) == 8:
        validcount += 1

    else:
        # records with 7 fields are invalid if they have a 'cid' field
        valid = True
        for field in record:
            if field.split(':')[0] == 'cid':
                valid = False
        if valid:
            validcount += 1

print(validcount)

# Part 2

validcount = 0
for record in data:

    if len(record) < 7:
        continue

    valid = True
    for field in record:

        key = field.split(':')[0]
        value = field.split(':')[1]

        if key == 'cid' and len(record) == 7:
            valid = False

        if key == 'byr':
            if int(value) < 1920 or int(value) > 2002:
                valid = False

        if key == 'iyr':
            if int(value) < 2010 or int(value) > 2020:
                valid = False

        if key == 'eyr':
            if int(value) < 2020 or int(value) > 2030:
                valid = False

        if key == 'hgt':
            if len(value) == 5:
                if value[3:5] != 'cm':
                    valid = False
                if int(value[0:3]) < 150 or int(value[0:3]) > 193:
                    valid = False
            elif len(value) == 4:
                if value[2:4] != 'in':
                    valid = False
                if int(value[0:2]) < 59 and int(value[0:2]) > 76:
                    valid = False
            else:
                valid = False

        if key == 'hcl':
            if len(value) != 7 or value[0] != '#':
                valid = False
            else:
                for char in range(1, 7):
                    if value[char] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                        valid = False

        if key == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid = False

        if key == 'pid':
            if len(value) != 9:
                valid = False
            else:
                for char in list(value):
                    if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        valid = False

    if valid:
        validcount += 1

print(validcount)