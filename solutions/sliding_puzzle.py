from queue import PriorityQueue

_target = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

def _get_distance(grid) -> int:
    distance = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                continue
            x, y = divmod(grid[i][j] - 1, 3)
            distance += abs(x - i) + abs(y - j)
    return distance

def sliding_puzzle(grid) -> int | None:
    pq = PriorityQueue()
    seen = set()
    if grid == _target:
        return 0

    pq.put((0, grid))

    while not pq.empty():
        distance, current_grid = pq.get()
        seen.add(tuple(map(tuple, current_grid)))

        if current_grid == _target:
            return distance

        i, j = 0, 0
        for i in range(3):
            for j in range(3):
                if current_grid[i][j] == 0:
                    break
            if current_grid[i][j] == 0:
                break

        for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= i + x < 3 and 0 <= j + y < 3:
                new_grid = [row.copy() for row in current_grid]
                new_grid[i][j], new_grid[i + x][j + y] = new_grid[i + x][j + y], new_grid[i][j]
                if tuple(map(tuple, new_grid)) not in seen:
                    pq.put((distance + 1, new_grid))

    return None
