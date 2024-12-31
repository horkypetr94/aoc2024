import pandas as pd


def read_combinations(file_name):
    data = []
    with open(file_name) as f:
        for line in f:
            splited_line = line.split("|")
            key = int(splited_line[0])
            value = int(splited_line[1])
            data.append({"key": key, "value": value})

    df = pd.DataFrame(data)

    return df


def read_pattern(file_name):
    pattern = []
    with open(file_name) as f:
        for line in f:
            char_pattern = []
            splited_line = line.split(",")
            for char in splited_line:
                char_pattern.append(int(char))
            pattern.append(char_pattern)

    return pattern


# comb_dict = read_combinations(file_name="pattern.txt")
# pattern = read_pattern(file_name="combinations_list.txt")
comb_dict = read_combinations(file_name="test_combinations_list.txt")
patterns = read_pattern(file_name="test_pattern.txt")


def search_key(df, key):
    return 1


count = 0
# for pattern in patterns:
#     for key in pattern:
