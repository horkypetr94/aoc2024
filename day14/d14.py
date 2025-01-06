import re
import numpy as np


def count_quadrants(arr):
    rows, cols = arr.shape
    row, col = rows // 2, cols // 2

    top_left = arr[:row, :col]
    top_right = arr[:row, -col:]
    bottom_left = arr[-row:, :col]
    bottom_right = arr[-row:, -col:]

    return (
        np.sum(top_left)
        * np.sum(top_right)
        * np.sum(bottom_left)
        * np.sum(bottom_right)
    )


n_iters = 100
size_x = 101
size_y = 103

with open("input.txt") as f:
    lines = f.readlines()

with open("output.txt", "w") as output:
    # Part 2
    # for n_iters in range(39, 10000, 101):
    array = np.zeros((size_y, size_x))
    for line in lines:
        numbers = re.findall(r"-?\d+", line)
        starting_position, velocity = (
            np.array(numbers[:2], dtype=int),
            np.array(numbers[2:], dtype=int),
        )
        end_position = starting_position + n_iters * velocity
        end_x = end_position[0] % size_x
        end_y = end_position[1] % size_y
        array[end_y, end_x] += 1

    # Part 2
    # array_str = np.where(array == 0, " ", "X")
    # np.savetxt(output, array_str, delimiter=" ", fmt="%s")
    # output.write("\n")
    # output.write(str(n_iters))
    # output.write(200*"#")

    count = count_quadrants(array)
    print(f"result 1: {count}")
    # 7412 is a tree
