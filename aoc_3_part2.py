def matching_char(s1, s2, s3):
    set2 = set(s2)
    set3 = set(s3)

    # Iterate through the characters in the first string
    for char in s1:
        if char in set2 and char in set3:
            return char


if __name__ == '__main__':

    sum_priorities = 0
    # f = open('aoc_3_test_data1.txt')
    f = open('aoc_3_data1.txt')
    ctr = 0

    for line in f:
        line = line.strip()
        if ctr == 0:
            first = line
            ctr += 1
        elif ctr == 1:
            second = line
            ctr += 1
        else:
            third = line
            ctr = 0
            ch = matching_char(first, second, third)
            if ch.islower():
                priority = ord(ch) - 96
            else:
                priority = ord(ch) - 38
            sum_priorities += priority

    f.close()
    print(sum_priorities)
    # 2760
