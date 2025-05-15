import sys
from collections import defaultdict

from aoc_tools import read_input_to_text_array


def get_dir_sizes(dir_tree, curr_dir):
    def get_size(curr_dir):
        dir_size = 0
        for e in dir_tree[curr_dir]:
            if e[0] == 'dir':
                dname, dsize = get_size(curr_dir + e[1] + '/')
                dir_size += dsize
            else:
                dir_size += int(e[0])
        dir_sizes[curr_dir] = dir_size
        return curr_dir, dir_size

    dir_sizes = defaultdict(int)
    get_size(curr_dir)
    return dir_sizes


# def get_dir_sizes(dir_tree, curr_dir):
#     def get_size(curr_dir):
#         dir_size = 0
#         for e in dir_tree[curr_dir]:
#             if e[0] == 'dir':
#                 dname, dsize = get_size(curr_dir + e[1] +'/')
#                 dir_size += dsize
#             else:
#                 dir_size += int(e[0])
#         dir_sizes.append((curr_dir, dir_size))
#         return curr_dir, dir_size
#
#     dir_sizes = []
#     get_size(curr_dir)
#     return dir_sizes


if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)
    # arr = read_input_to_text_array('aoc_7_test_data1.txt')
    arr = read_input_to_text_array('aoc_7_data1.txt')

    dir_tree = defaultdict(list)
    dir_stack = []
    curr_dir = ''

    for s in arr:
        if s.startswith('$ cd'):
            dir_name = s[5:]
            if dir_name == '..':
                last_dir = dir_stack.pop()
                curr_dir = dir_stack[-1]
            else:
                if dir_name == '/':
                    curr_dir = '/'
                else:
                    curr_dir += dir_name + '/'
                dir_stack.append(curr_dir)
        elif s.startswith('$ ls'):
            pass
        else:
            dir_info = s.split(' ')
            dir_tree[curr_dir].append((dir_info[0], dir_info[1]))

    # print(dir_tree)
    for k, v in dir_tree.items():
        print(k, v)
    print('end dir_tree')

    dir_sizes = get_dir_sizes(dir_tree, '/')
    for k, v in dir_sizes.items():
        print(k,v)
    print(sum(v for v in dir_sizes.values() if v <= 100_000))

    # part 2
    unused_space = 70_000_000 - 44965705

    min_sz = sys.maxsize
    for sz in dir_sizes.values():
        if sz + unused_space >= 30_000_000:
            min_sz = min(min_sz, sz)
    print(min_sz)
