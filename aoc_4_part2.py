from aoc_tools import read_input_to_nums

if __name__ == '__main__':

    # nums = read_input_to_nums('aoc_4_test_data1.txt')
    nums = read_input_to_nums('aoc_4_data1.txt')

    overlap_count = 0
    for e in nums:
        if e[0] in range(e[2], e[3] + 1) or e[1] in range(e[2], e[3] + 1) or e[2] in range(e[0], e[1] + 1) or e[3] in range(e[0], e[1] + 1):
            overlap_count += 1
            print(e)

print(overlap_count)
