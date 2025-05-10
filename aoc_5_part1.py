import re
from collections import deque

def read_input_to_sections_no_strip(in_file):
    f = open(in_file)
    sections = f.read().split('\n\n')
    f.close()
    return sections


def pad_trailing_spaces(s, slen):
    return s + ' ' * (slen - len(s))


if __name__ == '__main__':

    # sections = read_input_to_sections_no_strip('aoc_5_test_data1.txt')
    # sections = read_input_to_sections_no_strip('aoc_5_test_data2.txt')
    sections = read_input_to_sections_no_strip('aoc_5_data1.txt')

    txt_arr = [e for e in sections[0].split('\n')]
    nums = re.findall(r'\d+', txt_arr[len(txt_arr) - 1])  # last line - stack number - 1  2  3 ...
    stack_count = int(nums[-1])
    print('stack_count', stack_count)

    # 0   1
    # 1   5
    # 2   9
    # 3  13

    # create stacks
    stacks = [deque() for i in range(stack_count)]
    print(stacks)
    for txt in txt_arr:
        txt = pad_trailing_spaces(txt, stack_count * 4 - 1)
        if txt[1] != '1':  # ignore last line as these are just stack numbers
            for i in range(stack_count):
                idx = i * 4 + 1
                if txt[idx] != ' ':
                    stacks[i].appendleft(txt[idx])
    print(stacks)

    # move stacks
    for e in sections[1].split('\n'):
        nums = re.findall(r'\d+', e)
        nums = [int(num) for num in nums]
        crate_count, from_stack, to_stack = nums
        for _ in range(crate_count):
            stacks[to_stack-1].append(stacks[from_stack-1].pop())
    print(stacks)

    result = ''.join([e[-1] for e in stacks])  # get crates on top of stack
    print(result)