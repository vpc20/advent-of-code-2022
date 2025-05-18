from aoc_tools import read_input_to_text_array

if __name__ == '__main__':
    txt_arr = read_input_to_text_array('aoc_9_test_data1.txt')
    # txt_arr = read_input_to_text_array('aoc_9_data1.txt')

    txt = '''......
......
......
......
H.....'''

    grid = [[c for c in line] for line in txt.split('\n')]
    for e in grid:
        print(e)
    print()

    nrows = len(grid)
    ncols = len(grid[0])

    # initial positions of head and tail
    hpos = (nrows - 1, 0)
    tpos = (nrows - 1, 0)

    # positions visited by tail
    tpos_set = set()
    tpos_set.add(tpos)

    for e in txt_arr:
        direction, steps = e.split(' ')
        print(direction, steps)

    print(tpos_set)
