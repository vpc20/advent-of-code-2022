from collections import defaultdict

from aoc_tools import read_input_to_text_array

if __name__ == '__main__':

    arr = read_input_to_text_array('aoc_7_test_data1.txt')
    # arr = read_input_to_text_array('aoc_7_data1.txt')
    dir_size = defaultdict(int)
    dir_stack = []
    curr_dir = ''

    for s in arr:
        if s.startswith('$ cd'):
            dir_name = s[5:]
            if dir_name == '..':
                last_dir = dir_stack.pop()
                curr_dir = dir_stack[-1]
                dir_size[curr_dir] += dir_size[last_dir]
            else:
                curr_dir += dir_name + '/'
                dir_stack.append(curr_dir)
                dir_size[curr_dir] = 0
        elif s.startswith('$ ls'):
            pass
        else:
            dir_info = s.split(' ')
            if dir_info[0].isdigit():
                dir_size[curr_dir] += int(dir_info[0])

    dir_size['//'] += dir_size[dir_stack[-1]]  # because there is no cd .. after last directory is processed

    for k, v in dir_size.items():
        print(k, v)
    x = sum(v for k, v in dir_size.items() if v <= 100000)
    print(x)
