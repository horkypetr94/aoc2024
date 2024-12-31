from itertools import cycle


def move(position, direction, steps_counter):
    position[0] += movement[direction][0]
    position[1] += movement[direction][1]
    steps_counter[direction] += 1

    return position, steps_counter


def check_and_turn(position, direction, maze, cycle_count, steps_counter):
    search_area = position.copy()
    search_area[0] += movement[direction][0]
    search_area[1] += movement[direction][1]

    game_on = check_end_game(search_area, maze)

    if game_on:
        if maze[search_area[0]][search_area[1]] == "#":
            cycle_count += 1
            direction = next(direction_cycle)
            if cycle_count % 4 == 0:
                steps_counter = {"up": 0, "down": 0, "left": 0, "right": 0}
            return game_on, direction, cycle_count, steps_counter

    return game_on, direction, cycle_count, steps_counter


def check_end_game(position, maze):
    if (
        position[0] < 0
        or position[0] >= len(maze)
        or position[1] < 0
        or position[1] >= len(maze[0])
    ):
        return False
    return True


def check_paradox(paradox_counter, steps_counter):
    if (
        steps_counter["up"] == steps_counter["down"]
        and steps_counter["right"] < steps_counter["left"]
    ):
        paradox_counter += 1

    return paradox_counter


maze = []
with open("test.txt") as f:
    for line in f:
        maze.append(list(line.strip()))  # Strip newline and split into characters
# position = [52, 36]
position = [6, 4]
cycle_count = 0
direction_cycle = cycle(["up", "right", "down", "left"])
direction = next(direction_cycle)
movement = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
steps_counter = {
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0,
}
paradox_counter = 0

game_on = True
while game_on:
    position, steps_counter = move(position, direction, steps_counter)

    search_area = position.copy()
    search_area[0] += movement[direction][0]
    search_area[1] += movement[direction][1]

    game_on = check_end_game(search_area, maze)

    if game_on:
        if maze[search_area[0]][search_area[1]] == "#":
            cycle_count += 1
            direction = next(direction_cycle)
            if cycle_count % 4 == 0:
                paradox_counter = check_paradox(paradox_counter, steps_counter)
                steps_counter = {"up": 0, "down": 0, "left": 0, "right": 0}

    maze[position[0]][position[1]] = "X"


for line in maze:
    print(line)

S = sum([row.count("X") for row in maze])
print(S)
print(paradox_counter)
