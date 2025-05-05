def matching_char(s1, s2):
    set2 = set(s2)

    # Iterate through the characters in the first string
    for char in s1:
        if char in set2:
            return char

if __name__ == '__main__':

    sum_priorities = 0
    # f = open('aoc_3_test_data1.txt')
    f = open('aoc_3_data1.txt')

    for line in f:
        line = line.strip()
        mid = len(line) // 2
        first = line[:mid]
        second = line[mid:]
        print(first, second)
        ch = matching_char(first, second)
        if ch.islower():
            priority = ord(ch) - 96
        else:
            priority = ord(ch) - 38
        sum_priorities += priority

    f.close()
    print(sum_priorities)
