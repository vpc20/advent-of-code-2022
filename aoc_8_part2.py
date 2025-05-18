import math

from aoc_tools import read_input_to_grid_int

# def visible_from_right(grid, nrows, ncols, r, c):
#     return all(grid[r][c] > grid[r][dc] for dc in range(c + 1, ncols))


if __name__ == '__main__':
    # grid = read_input_to_grid_int('aoc_8_test_data1.txt')
    grid = read_input_to_grid_int('aoc_8_data1.txt')
    nrows = len(grid)
    ncols = len(grid[0])
    for e in grid:
        print(e)

    max_scenic_score = 0

    for r in range(1, nrows - 1):
        for c in range(1, ncols - 1):
            visible_counts = [0, 0, 0, 0]

            for dc in range(c - 1, -1, -1):
                visible_counts[0] += 1
                if grid[r][c] <= grid[r][dc]:
                    break

            for dc in range(c + 1, ncols):
                visible_counts[1] += 1
                if grid[r][c] <= grid[r][dc]:
                    break

            for dr in range(r - 1, -1, -1):
                visible_counts[2] += 1
                if grid[r][c] <= grid[dr][c]:
                    break

            for dr in range(r + 1, nrows):
                visible_counts[3] += 1
                if grid[r][c] <= grid[dr][c]:
                    break

            scenic_score = math.prod(visible_counts)
            max_scenic_score = max(max_scenic_score, scenic_score)

    print(max_scenic_score)
