from aoc_2_part1 import SCISSORS

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

if __name__ == '__main__':
    result_points_dict = {'X': 0, 'Y': 3, 'Z': 6}
    points_dict = {'A': 1, 'B': 2, 'C': 3}
    rps_dict = {(ROCK, LOSE): SCISSORS,
                (ROCK, DRAW): ROCK,
                (ROCK, WIN): PAPER,
                (PAPER, LOSE): ROCK,
                (PAPER, DRAW): PAPER,
                (PAPER, WIN): SCISSORS,
                (SCISSORS, LOSE): PAPER,
                (SCISSORS, DRAW): SCISSORS,
                (SCISSORS, WIN): ROCK
                }
    total_score = 0
    # f = open('aoc_2_test_data1.txt')
    f = open('aoc_2_data1.txt')

    for line in f:
        opp, me = line.strip().split(' ')
        # opp = rps_dict[opp]
        score = 0
        score = result_points_dict[me] + points_dict[rps_dict[(opp, me)]]
        print(score)
        total_score += score
    f.close()
    print(total_score)
    # 13448

# if opp == ROCK:
#     if me == 'X':  # lose
#         score = 0 + points_dict[SCISSORS]
#     elif me == 'Y':  # draw
#         score = 3 + points_dict[ROCK]
#     else:  # win
#         score = 6 + points_dict[PAPER]
# elif opp == PAPER:
#     if me == 'X':  # lose
#         score = 0 + points_dict[ROCK]
#     elif me == 'Y':  # draw
#         score = 3 + points_dict[PAPER]
#     else:  # win
#         score = 6 + points_dict[SCISSORS]
# elif opp == SCISSORS:
#     if me == 'X':  # lose
#         score = 0 + points_dict[PAPER]
#     elif me == 'Y':  # draw
#         score = 3 + points_dict[SCISSORS]
#     else:  # win
#         score = 6 + points_dict[ROCK]
