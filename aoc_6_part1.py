if __name__ == '__main__':

    # f = open('aoc_6_test_data1.txt')
    f = open('aoc_6_data1.txt')

    s = f.read()
    print(s)
    print(len(s))

    for i in range(len(s) - 4):
        s4 = s[i:i + 4]
        if len(s4) == len(set(s4)):
            print(i + 4)
            break

    f.close()
