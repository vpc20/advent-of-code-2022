from aoc_tools import print_grid_as_text

if __name__ == '__main__':
    grid = [['.'] * 600 for e in range(200)]
    # for e in grid:
    #     print(e)

    # draw rocks
    # f = open('aoc_14_test_data1.txt')
    f = open('aoc_14_data1.txt')

    for line in f:
        arr = [e.split(',') for e in line.strip().split(' -> ')]
        print(arr)
        first = arr[0]
        second = arr[1]

        first0 = int(first[0])
        first1 = int(first[1])
        second0 = int(second[0])
        second1 = int(second[1])

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

        for e in arr[2:]:
            first = second
            second = e
            first0 = int(first[0])
            first1 = int(first[1])
            second0 = int(second[0])
            second1 = int(second[1])
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

    print_grid_as_text(grid)

    f.close()
