from tqdm import tqdm


def rules(item: str) -> list[str]:
    if item == "0":
        return ["1"]
    elif len(item) % 2 == 0:
        half = int(len(item) / 2)
        return [item[:half], str(int(item[half:]))]
    else:
        return [str(int(item) * 2024)]


new_array = ["510613", "358", "84", "40702", "4373582", "2", "0", "1584"]
blinks = 25
for i in tqdm(range(blinks)):
    input_sequence = new_array
    new_array = []
    for s in input_sequence:
        new_array.extend(rules(s))

print(f"Result: {len(new_array)}")
