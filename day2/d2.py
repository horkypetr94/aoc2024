def parse_input(filename: str) -> list:
    array = []
    with open(filename) as f:
        for line in f:
            inner_array = []
            for char in line.split():
                inner_array.append(int(char))
            array.append(inner_array)
    return array


def _is_sequence_valid(line):
    for i in range(len(line) - 1):
        if not line[i + 1] - 3 <= line[i] <= line[i + 1] + 3:
            return False
    return True


def extend_input(array):
    extended_array = []
    for line in array:
        inner_array = []
        inner_array.append(line)
        for i, _ in enumerate(line):
            line_copy = line.copy()
            line_copy.pop(i)
            inner_array.append(line_copy)
        extended_array.append(inner_array)

    return extended_array


array = parse_input("input.txt")
count = 0

# part 2
array = extend_input(array)

for line_set in array:
    for line in line_set:
        if len(set(line)) == len(line):
            if line == sorted(line) or line == sorted(line, reverse=True):
                if _is_sequence_valid(line):
                    count += 1
                    break

print(count)
