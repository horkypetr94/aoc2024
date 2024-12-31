import numpy as np


def find_x(arr):
    count = 0
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            if arr[i, j] == "M":
                if (
                    arr[i, j + 2] == "S"
                    and arr[i + 1, j + 1] == "A"
                    and arr[i + 2, j] == "M"
                    and arr[i + 2, j + 2] == "S"
                ):
                    count += 1
                if (
                    arr[i, j + 2] == "M"
                    and arr[i + 1, j + 1] == "A"
                    and arr[i + 2, j] == "S"
                    and arr[i + 2, j + 2] == "S"
                ):
                    count += 1
            elif arr[i, j] == "S":
                if (
                    arr[i, j + 2] == "S"
                    and arr[i + 1, j + 1] == "A"
                    and arr[i + 2, j] == "M"
                    and arr[i + 2, j + 2] == "M"
                ):
                    count += 1
                if (
                    arr[i, j + 2] == "M"
                    and arr[i + 1, j + 1] == "A"
                    and arr[i + 2, j] == "S"
                    and arr[i + 2, j + 2] == "M"
                ):
                    count += 1
    return count


input_text = []
with open("input.txt") as f:
    for line in f:
        input_text.append(list(line[:-1]))
arr = np.array(input_text)

print(find_x(arr))
