line = [510613, 358, 84, 40702, 4373582, 2, 0, 1584]


def rules(n: int) -> list[int]:
    n_str = str(n)
    if n == 0:
        return [1]
    elif len(n_str) % 2 == 0:
        half = int(len(n_str) / 2)
        return [int(n_str[:half]), int(n_str[half:])]
    else:
        return [n * 2024]


line_dict = dict((n, 1) for n in line)
for i in range(75):
    tmp = dict()
    for num, n in line_dict.items():
        for n_new in rules(num):
            if n_new in tmp:
                tmp[n_new] += n
            else:
                tmp[n_new] = n

    line_dict = tmp

result = sum(n for n in line_dict.values())
print("result " + str(result))
