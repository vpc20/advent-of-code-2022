from aoc_tools import read_input_to_sections

if __name__ == '__main__':
    sections = read_input_to_sections('aoc_1_data1.txt')

    max_sum = 0
    for calories_str in sections:
        sum_cal = sum(int(calory.strip()) for calory in calories_str.split('\n'))
        max_sum = max(max_sum, sum_cal)
    print(max_sum)
