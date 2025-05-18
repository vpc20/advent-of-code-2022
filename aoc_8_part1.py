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

    visible_edge_count = nrows * 2 + (ncols - 2) * 2
    print(visible_edge_count)

    visible_count = 0
    for r in range(1, nrows - 1):
        for c in range(1, ncols - 1):
            if all(grid[r][c] > grid[r][dc] for dc in range(0, c)) \
                    or all(grid[r][c] > grid[r][dc] for dc in range(c + 1, ncols)) \
                    or all(grid[r][c] > grid[dr][c] for dr in range(0, r)) \
                    or all(grid[r][c] > grid[dr][c] for dr in range(r + 1, nrows)):
                visible_count += 1
            # else:
            #     print('not visible',r,c,grid[r][c])
    print(visible_count)
    print(visible_edge_count+ visible_count)