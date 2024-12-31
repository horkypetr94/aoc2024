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


def calculate_nodes(vecs, array_len):
    magnitude = vecs[0] - vecs[1]
    all_nodes = []

    # Forward from vecs[0]
    while 0 <= vecs[0][0] < array_len and 0 <= vecs[0][1] < array_len:
        all_nodes.append(tuple(vecs[0]))
        vecs[0] = vecs[0] + magnitude

    # Backward from vecs[1]
    while 0 <= vecs[1][0] < array_len and 0 <= vecs[1][1] < array_len:
        all_nodes.append(tuple(vecs[1]))
        vecs[1] = vecs[1] - magnitude

    return all_nodes


chars = np.unique(array)
unique_chars = chars[chars != "."]
unique_chars = unique_chars[unique_chars != "#"]
antinode_positions = []

for char in unique_chars:
    combos = create_combinations(array, char)

    for combo in combos:
        vecs = np.array(combo)
        pos = calculate_nodes(vecs, len(array))
        antinode_positions = [*antinode_positions, *pos]

print(len(set(antinode_positions)))
