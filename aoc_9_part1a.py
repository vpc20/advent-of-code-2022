from aoc_tools import read_input_to_text_array

if __name__ == '__main__':
    # txt_arr = read_input_to_text_array('aoc_9_test_data1.txt')
    txt_arr = read_input_to_text_array('aoc_9_data1.txt')

    # initial positions of head and tail
    hrow = 0
    hcol = 0
    trow = 0
    tcol = 0

    # positions visited by tail
    tpos_set = set()
    tpos_set.add((0, 0))

    for e in txt_arr:
        direction, steps = e.split(' ')
        steps = int(steps)
        print(direction, steps)

        for _ in range(steps):
            if direction == 'L':
                if (hrow == trow + 1 and tcol == hcol + 1) or (trow == hrow + 1 and tcol == hcol + 1):
                    hcol -= 1
                    trow = hrow
                    tcol = hcol + 1
                elif hrow == trow and tcol == hcol + 1:
                    hcol -= 1
                    tcol -= 1
                else:
                    hcol -= 1
            elif direction == 'R':
                if (trow == hrow + 1 and hcol == tcol + 1) or (hrow == trow + 1 and hcol == tcol + 1):
                    hcol += 1
                    trow = hrow
                    tcol = hcol - 1
                elif hrow == trow and hcol == tcol + 1:
                    hcol += 1
                    tcol += 1
                else:
                    hcol += 1
            elif direction == 'U':
                if (hrow == trow + 1 and hcol == tcol + 1) or (hrow == trow + 1 and tcol == hcol + 1):
                    hrow += 1
                    trow = hrow - 1
                    tcol = hcol
                elif hcol == tcol and hrow == trow + 1:
                    hrow += 1
                    trow += 1
                else:
                    hrow += 1
            elif direction == 'D':
                if (trow == hrow + 1 and hcol == tcol + 1) or (trow == hrow + 1 and tcol == hcol + 1):
                    hrow -= 1
                    trow = hrow + 1
                    tcol = hcol
                elif hcol == tcol and trow == hrow + 1:
                    hrow -= 1
                    trow -= 1
                else:
                    hrow -= 1

            print((hrow, hcol),(trow, tcol))
            tpos_set.add((trow, tcol))

    print(tpos_set)
    print(len(tpos_set))
