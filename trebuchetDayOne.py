# iterate through the arr of string
# isolate any ints in string
# isolate first and last ints in string
# combine them to make a two-digit num
# append two-digit num into a sum
# return sum

import re

sum = 0
with open('trebuchetPuzzleInput.txt', 'r') as file:
    puzzle_input = file.read().split('\n')

for line in puzzle_input:
    digits = re.findall(r'\d', line)
    sum += int(digits[0] + digits[-1])
print(sum)
