# read file, isolate into integer and string pairs
# determine amount of blue, green, and red cubes in each line
# compare these amounts to the amount defined by the problem

with open('dayTwoPuzzleInput.txt', 'r') as file:
    puzzle_input = file.read().split('\n')

# seek possible games with this amout of each cube
target_red_cubes = 12
target_green_cubes = 13
target_blue_cubes = 14

for line in puzzle_input:
    