from aoc_tools import read_input_to_text_array

if __name__ == '__main__':
    # txt_arr = read_input_to_text_array('aoc_9_test_data1.txt')
    txt_arr = read_input_to_text_array('aoc_9_data1.txt')

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
    # hpos = (nrows - 1, 0)
    # tpos = (nrows - 1, 0)
    hrow = nrows - 1
    hcol = 0
    trow = nrows - 1
    tcol = 0

    # positions visited by tail
    tpos_set = set()
    tpos_set.add((trow, tcol))

    for e in txt_arr:
        direction, steps = e.split(' ')
        steps = int(steps)
        print(direction, steps)

        for _ in range(steps):
            if direction == 'L':
                if hcol > 0:
                    if (hrow == trow - 1 and hcol == tcol - 1) or (hrow == trow + 1 and hcol == tcol - 1):
                        hcol -= 1
                        trow = hrow
                        tcol = hcol + 1
                    elif hrow == trow and tcol == hcol + 1:
                        hcol -= 1
                        tcol -= 1
                    else:
                        hcol -= 1
            elif direction == 'R':
                if hcol < ncols - 1:
                    if (hrow == trow - 1 and hcol == tcol + 1) or (hrow == trow + 1 and hcol == tcol + 1):
                        hcol += 1
                        trow = hrow
                        tcol = hcol - 1
                    elif hrow == trow and tcol == hcol - 1:
                        hcol += 1
                        tcol += 1
                    else:
                        hcol += 1
            elif direction == 'U':
                if hrow > 0:
                    if (hrow == trow - 1 and hcol == tcol + 1) or (hrow == trow - 1 and hcol == tcol - 1):
                        hrow -= 1
                        trow = hrow + 1
                        tcol = hcol
                    elif hcol == tcol and trow == hrow + 1:
                        hrow -= 1
                        trow -= 1
                    else:
                        hrow -= 1
            elif direction == 'D':
                if hrow < nrows - 1:
                    if (hrow == trow + 1 and hcol == tcol - 1) or (hrow == trow + 1 and hcol == tcol + 1):
                        hrow += 1
                        trow = hrow + 1
                        tcol = hcol
                    elif hcol == tcol and trow == hrow - 1:
                        hrow += 1
                        trow += 1
                    else:
                        hrow += 1

            tpos_set.add((trow, tcol))

            temp_grid = [['.' for j in range(ncols)] for i in range(nrows)]
            temp_grid[trow][tcol] = 'T'
            temp_grid[hrow][hcol] = 'H'
            for e in temp_grid:
                print(e)
            print()

    print(tpos_set)
    print(len(tpos_set))
