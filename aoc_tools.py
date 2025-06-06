import re
from collections import defaultdict


def read_input_to_grid(in_file):
    f = open(in_file)
    result = [[c for c in line.strip()] for line in f]
    f.close()
    return result


def read_input_to_grid_int(in_file):
    f = open(in_file)
    result = [[int(c) for c in line.strip()] for line in f]
    f.close()
    return result


def read_input_to_text_array(in_file):
    f = open(in_file)
    result = [line.strip() for line in f]
    f.close()
    return result


def read_input_to_list_of_grids(in_file):
    f = open(in_file)
    blocks = f.read().strip().split('\n\n')
    grids = []
    for block in blocks:
        rows = block.splitlines()
        grid = [list(row) for row in rows]
        grids.append(grid)
    f.close()
    return grids


def read_input_to_nums(in_file):  # use this if there are charactes in the input which need to be filtered out
    f = open(in_file)
    nums = [re.findall(r'\d+', line) for line in f]
    result = [[int(n) for n in num] for num in nums]  # covert to numbers
    f.close()
    return result

def read_input_to_nums_neg(in_file):  # use this if there are charactes in the input which need to be filtered out
    f = open(in_file)
    nums = [re.findall(r'-*\d+', line) for line in f]  # include negative numbers
    result = [[int(n) for n in num] for num in nums]  # covert to numbers
    f.close()
    return result


def read_input_to_nums1(in_file):  # use this if all the inputs are numbers only
    f = open(in_file)
    result = [[int(num) for num in line.strip().split()] for line in f]
    f.close()
    return result


def read_input_to_sections(in_file):
    f = open(in_file)
    sections = f.read().strip().split('\n\n')
    f.close()
    return sections


def read_text_to_nums(text):
    # nums = [re.findall(r'\d+', line) for line in text.split('\n')]
    nums = []
    for line in text.split('\n'):
        regex_nums = re.findall(r'\d+', line)
        if regex_nums:
            nums.append(regex_nums)
    result = [[int(n) for n in num] for num in nums]
    return result


def print_grid(arr):
    for e in arr:
        print(e)
    print()


def print_grid_with_tabs(arr):
    for e in arr:
        print(*e, sep='\t')
    print()


def print_grid_as_text(arr):
    for e in arr:
        print(''.join(c for c in e))
    print()


def print_text_array(arr):
    for e in arr:
        print(e)
    print()


def create_graph_from_grid(grid):
    g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(grid)
    ncols = len(grid[0])

    for r in range(nrows):
        for c in range(ncols):
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    # if grid[r][c] == grid[nr][nc]:  # if grouped by same values in each cell
                    #     g[(r, c)].append((nr, nc))
                    # if grid[r][c] == grid[nr][nc]:  # if obstructions needs to be removed, e.g. maze problems
                    #     g[(r, c)].append((nr, nc))
                    g[(r, c)].append((nr, nc))
            else:
                _ = g[(r, c)]  # create empty list, use _ instead of dummy variable
    return g


if __name__ == '__main__':
    # grid = read_input_to_grid('input.txt')
    # print_grid(grid)
    # print_grid_as_text(grid)
    #
    # x = read_input_to_nums('aoc_13_test_data1.txt')
    # print(x)
    # print_grid(x)
    #
    # x = read_input_to_nums('aoc_2_test_data1.txt')
    # print_grid(x)
    # print_grid_with_tabs(x)

    # sections = read_input_to_sections('aoc_5_test_data1.txt')
    # for section in sections:
    #     print(section)
    #     print()
    #     print(read_text_to_nums(section))

    # print(read_text_to_nums(section[0]))

    nums = read_input_to_nums('input.txt')
    print(nums)
