from helpers.loading_tools import load_numpy_array

input_array = load_numpy_array("test.txt")

GridPoint = tuple[int, int]
IntGrid = dict[GridPoint, int]


def score_trailhead(grid: IntGrid, trailhead: GridPoint) -> int:
    score = 0
    visited: set[GridPoint] = set()

    queue: list[GridPoint] = [trailhead]  # 1

    while queue:  # 2
        cur = queue.pop()  # 2

        if cur in visited:  # 3
            continue

        visited.add(cur)  # 4

        if (val := grid[cur]) == 9:  # 5
            score += 1
            continue

        queue.extend(  # 6
            n for n in neighbors(cur, num_directions=4) if grid.get(n) == val + 1
        )
        # 7 - now we loop

    return score
