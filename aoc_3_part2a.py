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
    rucksacks = [None] * 3

    for line in f:
        line = line.strip()
        i = ctr % 3
        rucksacks[i] = line
        if i == 2:
            ch = matching_char(*rucksacks)
            if ch.islower():
                priority = ord(ch) - 96
            else:
                priority = ord(ch) - 38
            sum_priorities += priority
        ctr += 1

    f.close()
    print(sum_priorities)
