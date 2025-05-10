import re


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
    stacks_data = sections[0]
    movement_data = sections[1]

    txt_arr = [e for e in stacks_data.split('\n')]
    stack_count = (len(txt_arr[-1]) + 2) // 4
    print('stack_count', stack_count)

    # 0   1
    # 1   5
    # 2   9
    # 3  13

    # create stacks
    stacks = [[] for i in range(stack_count)]
    print(stacks)
    for txt in reversed(txt_arr[:-1]):
        txt = pad_trailing_spaces(txt, stack_count * 4 - 1)
        for i in range(stack_count):
            idx = i * 4 + 1
            if txt[idx] != ' ':
                stacks[i].append(txt[idx])
    print(stacks)

    # move stacks
    for e in movement_data.split('\n'):
        nums = re.findall(r'\d+', e)
        nums = [int(num) for num in nums]
        crate_count, from_stack, to_stack = nums
        for _ in range(crate_count):
            stacks[to_stack - 1].append(stacks[from_stack - 1].pop())
    print(stacks)

    result = ''.join([e[-1] for e in stacks])  # get crates on top of stack
    print(result)
