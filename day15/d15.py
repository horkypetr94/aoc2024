import numpy as np

instructions = []
with open("instructions.txt") as inst:
    for line in inst:
        instructions.extend(line.strip())


def load_numpy_array(filename):
    with open(filename) as f:
        array = [list(line.strip()) for line in f]
    return np.array(array)

input_array = load_numpy_array("maze.txt")
start_x, start_y = np.where(input_array == "@")
position = np.array((start_x[0], start_y[0]))

def translate_instructions(instruction):
    if instruction == "^":
        return np.array((-1,0))
    elif instruction == "v":
        return  np.array((1,0))
    elif instruction == "<":
        return  np.array((0,-1))
    elif instruction == ">":
        return  np.array((0,1))

for instruction in instructions:
    movement = translate_instructions(instruction)
    position += movement
    if input_array[tuple(position)] == "O":
        print("kamen")


