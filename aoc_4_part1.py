from aoc_tools import read_input_to_nums

if __name__ == '__main__':

    # nums = read_input_to_nums('aoc_4_test_data1.txt')
    nums = read_input_to_nums('aoc_4_data1.txt')

    overlap_count = 0
    for e in nums:
        if (e[0] >= e[2] and e[1] <= e[3]) or (e[2] >= e[0] and e[3] <= e[1]):
            overlap_count += 1
            print(e)

print(overlap_count)

# 512 - incorrect
# 269 - incorrect
