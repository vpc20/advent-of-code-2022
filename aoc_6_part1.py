# MARKER_LENGTH = 4  # part1
MARKER_LENGTH = 14  # part 2

if __name__ == '__main__':

    # f = open('aoc_6_test_data1.txt')
    f = open('aoc_6_data1.txt')

    s = f.read()
    print(s)
    print(len(s))

    for i in range(len(s) - MARKER_LENGTH):
        s4 = s[i:i + MARKER_LENGTH]
        if len(s4) == len(set(s4)):
            print(i + MARKER_LENGTH)
            break

    f.close()
