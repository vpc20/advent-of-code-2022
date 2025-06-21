from collections import defaultdict, deque

if __name__ == '__main__':
    f = open('aoc_10_test_data1.txt')
    # f = open('aoc_10_test_data2.txt')

    cycle = 0
    d = defaultdict(int)
    q1 = deque()
    q2 = deque()

    xreg = 1

    for line in f:
        instructions = line.strip().split(' ')
        inst = instructions[0]
        val = int(instructions[1]) if instructions[0] == 'addx' else ''

        cycle += 1
        print(f'\ncycle: {cycle}')

        if q1:
            q2.append(q1.popleft())
        if val:
            q1.append((inst, val))
        if q2:
            inst, val = q2.popleft()
            xreg += val
        print(f'xreg = {xreg}')

    while q1 or q2:
        cycle += 1
        print(f'\ncycle: {cycle}')

        if q1:
            q2.append(q1.popleft())
            if len(q2) == 1:
                print(f'xreg = {xreg}')
                continue
        if q2:
            inst, val = q2.popleft()
            xreg += val

        print(f'xreg = {xreg}')

    f.close()
