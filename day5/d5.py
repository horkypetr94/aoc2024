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


def search_values(df, value):
    df = df[df["key"] == value]
    return df["value"].values


# comb_dict = read_combinations(file_name="pattern.txt")
# pattern = read_pattern(file_name="combinations_list.txt")
df = read_combinations(file_name="combinations_list.txt")
patterns = read_pattern(file_name="pattern.txt")

count_total = 0
count_wrong = 0
for pattern in patterns:
    middle_index = len(pattern) // 2
    count_total += pattern[middle_index]
    for i, p in enumerate(pattern):
        values = search_values(df, p)
        vals_to_check = pattern[i + 1 :]
        if not set(vals_to_check).issubset(values):
            count_wrong += pattern[middle_index]
            break

print(f"Task 1: {count_total-count_wrong}")
