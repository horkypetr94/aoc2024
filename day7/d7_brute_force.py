from itertools import product

results = []
numbers = []

with open("input.txt") as f:
    for line in f:
        result, nums = line.split(":")
        results.append(int(result))
        n_line = []
        for n in nums.split():
            n_line.append(n)
        numbers.append(n_line)

summary = 0
for result, line in zip(results, numbers):
    combinations = ["".join(p) for p in product("*+|", repeat=len(line) - 1)]
    for combination in combinations:
        base = int(line[0])
        for val, c in zip(line[1:], combination):
            if c == "*":
                base *= int(val)
            elif c == "+":
                base += int(val)
            elif c == "|":
                base = int(str(base) + str(val))

        if result == base:
            summary += result
            break

print(summary)
