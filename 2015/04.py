# https://adventofcode.com/2015/day/4

from hashlib import md5

# input not from a file this time
key = 'ckczppom'

number = 0
result = ''
done5 = False

while result[0:6] != '000000':
    number += 1
    input = key + str(number)
    result = md5(input.encode()).hexdigest()
    if done5 == False and result[0:5] == '00000':
        print('5 zeroes:', number)
        done5 = True

print('6 zeroes:', number)
