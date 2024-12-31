import numpy as np

XMAS = "XMAS"
XMAS_R = "SAMX"


def count_xmas(line):
    local_count = 0
    local_count += line.count(XMAS)
    local_count += line.count(XMAS_R)

    return local_count


def horizontal_count(input_text):
    local_count = 0
    for i, _ in enumerate(input_text):
        joined_line = "".join(input_text[i, :])
        local_count += count_xmas(joined_line)

    return local_count


def vertical_count(input_text):
    local_count = 0
    for i, _ in enumerate(input_text):
        joined_line = "".join(input_text[:, i])
        local_count += count_xmas(joined_line)

    return local_count


def diagonal_count(arr):
    local_count = 0

    for offset in range(-arr.shape[0] + 1, arr.shape[1]):
        diagonal = np.diagonal(arr, offset=offset)
        joined_line = "".join(diagonal)
        local_count += count_xmas(joined_line)

        anti_diagonal = np.diagonal(np.fliplr(arr), offset=offset)
        joined_line = "".join(anti_diagonal)
        local_count += count_xmas(joined_line)

    return local_count


global_sum = 0
input_text = []
with open("test.txt") as f:
    for line in f:
        input_text.append(list(line[:-1]))
arr = np.array(input_text)

global_sum += horizontal_count(arr)
global_sum += vertical_count(arr)
global_sum += diagonal_count(arr)

print(global_sum)
