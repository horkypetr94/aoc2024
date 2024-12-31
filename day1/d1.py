import numpy as np
from collections import defaultdict


def parse_input(filename: str) -> tuple[list, list]:
    col_1 = []
    col_2 = []
    with open(filename) as f:
        for line in f:
            col_1.append(int(line.split()[0]))
            col_2.append(int(line.split()[1]))

    return col_1, col_2


def calculate_distance(col_left: list, col_right: list) -> float:
    col_diff = np.subtract(sorted(col_left), sorted(col_right))
    res = np.sum(abs(col_diff))
    return res


def calculate_uniques(col_left: list, col_right: list) -> float:
    sum = 0
    unique, counts = np.unique(col_right, return_counts=True)
    unique_dict = defaultdict(int, zip(unique, counts))
    for val in col_left:
        sum += unique_dict[val] * val

    return sum


col_left, col_right = parse_input("input.txt")
result_1 = calculate_distance(col_left, col_right)
result_2 = calculate_uniques(col_left, col_right)

print(result_1, result_2)
