# https://adventofcode.com/2022/day/6

with open('./06data.txt') as datafile:
    input = datafile.readline()

def findstring(stringlength):
    for i in range(len(input)):
        if len(set(input[i:i + stringlength])) == stringlength:
            return(i + stringlength)

print(findstring(4))
print(findstring(14))