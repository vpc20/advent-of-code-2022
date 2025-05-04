from aoc_tools import read_input_to_sections

if __name__ == '__main__':
    sections = read_input_to_sections('aoc_1_data1.txt')

    sum_list = []
    for calories_str in sections:
        cal_sum = sum(int(calory.strip()) for calory in calories_str.split('\n'))
        sum_list.append(cal_sum)

    sum_list.sort(reverse=True)
    print(sum_list[0] + sum_list[1] + sum_list[2])
