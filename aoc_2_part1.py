ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

if __name__ == '__main__':
    rps_dict = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    points_dict = {'X': 1, 'Y': 2, 'Z': 3}

    total_score = 0
    # f = open('aoc_2_test_data1.txt')
    f = open('aoc_2_data1.txt')

    for line in f:
        opp, me = line.strip().split(' ')
        opp = rps_dict[opp]
        score = 0
        if me == opp:
            score = 3 + points_dict[me]
        else:
            score = 0 + points_dict[me] if (me == ROCK and opp == PAPER) or (me == PAPER and opp == SCISSORS) or (
                    me == SCISSORS and opp == ROCK) else 6 + points_dict[me]
        print(score)
        total_score += score
    f.close()
    print(total_score)
    # 13924
