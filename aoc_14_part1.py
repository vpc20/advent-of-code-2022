import sys

from aoc_tools import print_grid_as_text


def print_grid(first, second):
    first0 = first[0]
    first1 = first[1]
    second0 = second[0]
    second1 = second[1]
    if first0 == second0:
        minval = min(first1, second1)
        maxval = max(first1, second1)
        for i in range(minval, maxval + 1):
            grid[i][first0] = '#'
    else:
        minval = min(first0, second0)
        maxval = max(first0, second0)
        for i in range(minval, maxval + 1):
            grid[first1][i] = '#'


if __name__ == '__main__':
    f = open('aoc_14_data1.txt')
    minx = sys.maxsize
    maxx, maxy = -sys.maxsize, -sys.maxsize
    xy_coords = []

    for line in f:
        arr = [e.split(',') for e in line.strip().split(' -> ')]
        inner_arr = []
        for e in arr:
            x = int(e[0])
            y = int(e[1])
            inner_arr.append((x, y))
            minx = min(minx, x)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
        xy_coords.append(inner_arr)
    print('minx', minx)
    print('maxx', maxx)
    print('maxy', maxy)

    print(xy_coords)
    grid = [['.'] * (maxx + 1) for e in range(maxy + 1)]
    f.close()

    for arr in xy_coords:
        first = arr[0]
        second = arr[1]
        print_grid(first, second)

        for e in arr[2:]:
            first = second
            second = e
            print_grid(first, second)

    print_grid_as_text(grid)
