from math import prod

SLOPES_TO_CHECK = ((1,1), (3, 1), (5, 1), (7, 1), (1, 2))

with open("day3-input.txt") as file:
    data = file.readlines()

map_width = len(data[0]) - 1

def check_slope(right, down):
    # start in x_position 0
    x_position = 0
    tree_count = 0

    # move down by down
    for row in data[down::down]:
        # move across right and use modulus to wrap
        x_position = (x_position + right) % map_width
        # check if new position is a tree and increment count
        if row[x_position] == "#":
            tree_count += 1
    return tree_count

print(prod([check_slope(*slope) for slope in SLOPES_TO_CHECK]))
