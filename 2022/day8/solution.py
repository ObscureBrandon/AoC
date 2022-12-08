from math import prod

with open("input.txt") as f:
    lines = f.read().splitlines()

grid: list[list[int]] = [[int(char) for char in l] for l in lines]

def is_visible(x: int, y: int) -> bool:
    # is the point (x, y) on the edges
    if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
        return True

    # get all the points above point (x, y)
    points_above = [(x, y) for y in range(y - 1, -1, -1)]
    # get all the points below point (x, y)
    points_below = [(x, y) for y in range(y + 1, len(grid[0]))]
    # get all the points to the left of point (x, y)
    points_left = [(x, y) for x in range(x - 1, -1, -1)]
    # get all the points to the right of point (x, y)
    points_right = [(x, y) for x in range(x + 1, len(grid))]

    return any(all(grid[x][y] > grid[i][j] for i, j in points) for points in [points_above, points_below, points_left, points_right])

def scenic_score(x: int, y: int) -> int:
    # get all the points above point (x, y)
    points_above = [(x, y) for y in range(y - 1, -1, -1)]
    # get all the points below point (x, y)
    points_below = [(x, y) for y in range(y + 1, len(grid[0]))]
    # get all the points to the left of point (x, y)
    points_left = [(x, y) for x in range(x - 1, -1, -1)]
    # get all the points to the right of point (x, y)
    points_right = [(x, y) for x in range(x + 1, len(grid))]

    ans = [0, 0, 0, 0]
    for point in points_above:
        ans[0] += 1
        if grid[point[0]][point[1]] >= grid[x][y]:
            break

    for point in points_below:
        ans[1] += 1
        if grid[point[0]][point[1]] >= grid[x][y]:
            break

    for point in points_left:
        ans[2] += 1
        if grid[point[0]][point[1]] >= grid[x][y]:
            break

    for point in points_right:
        ans[3] += 1
        if grid[point[0]][point[1]] >= grid[x][y]:
            break

    return prod(ans)

def part_1() -> int:
    return sum(is_visible(x, y) for x in range(len(grid)) for y in range(len(grid[0])))

def part_2() -> int:
    return max(scenic_score(x, y) for x in range(len(grid)) for y in range(len(grid[0])))
