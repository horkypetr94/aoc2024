
with open("input.txt") as f:
    input_string = f.readline()


def decode_sequence(s):
    value_list = []
    for i in range(0, 20000, 20):
        value_list.append(s[i : i + 20])
    return s


sequence = decode_sequence(input_string)
