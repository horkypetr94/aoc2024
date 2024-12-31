import re

with open("input.txt") as f:
    s = f.read()


def sum_muls(input_string):
    local_sum = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input_string)
    for match in matches:
        local_sum += int(match[0]) * int(match[1])
    return local_sum


sum_total = 0
for dont in s.split("don't()")[1:]:
    if "do()" in dont:
        dos = dont.split("do()")
        for do in dos[1:]:
            sum_total += sum_muls(do)


sum_total += sum_muls(s.split("don't()")[0])
# 72948684
print(sum_total)
