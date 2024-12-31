import numpy as np
from itertools import combinations

array = []
with open("input.txt") as f:
    for line in f:
        array.append(list(line.strip()))
array = np.array(array)


def create_combinations(array, char):
    rows, columns = np.where(array == char)
    if len(rows) < 2:
        return []
    coords = [(row, column) for row, column in zip(rows, columns)]
    return list(combinations(coords, 2))


def check_valid(value, array_len):
    if 0 <= value[0] < array_len and 0 <= value[1] < array_len:
        return tuple(value)
    return (array_len + 1, array_len + 1)


chars = np.unique(array)
unique_chars = chars[chars != "."]
unique_chars = unique_chars[unique_chars != "#"]
antinode_positions = []

for char in unique_chars:
    combos = create_combinations(array, char)

    for combo in combos:
        vecs = np.array(combo)
        magnitude = vecs[0] - vecs[1]
        top = vecs[0] + magnitude
        bottom = vecs[1] - magnitude
        antinode_positions.append(check_valid(top, len(array)))
        antinode_positions.append(check_valid(bottom, len(array)))

print(len(set(antinode_positions)) - 1)
