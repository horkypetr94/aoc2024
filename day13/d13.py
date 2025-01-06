import math

import numpy as np
import re


def get_solution(array, result):
    array
    solution = np.linalg.solve(array, result)
    return solution


def is_whole_number(solution):
    if math.isclose(np.round(solution[0], 2) % 1, 0) and math.isclose(
        np.round(solution[1], 2) % 1, 0
    ):
        return True
    return False


price = 0
with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        if i % 4 == 0:
            numbers = re.findall(r"\d+", line)
            array = np.zeros((2, 2))
            array[0, 0] = int(numbers[0])
            array[1, 0] = int(numbers[1])
        elif i % 4 == 1:
            numbers = re.findall(r"\d+", line)
            array[0, 1] = int(numbers[0])
            array[1, 1] = int(numbers[1])
        elif i % 4 == 2:
            numbers = re.findall(r"\d+", line)
            result = np.array([numbers[0], numbers[1]], dtype=float)
            result += np.array([10000000000000, 10000000000000])
            solution = get_solution(array, result)
            if is_whole_number(solution):
                price += solution[0] * 3 + solution[1]

print(price)
