from itertools import product
from random import randrange
from strategy import Strategy
from util import *
from os import system
from logging import *

s = Strategy()
strategies = s.strategies
strategies_name = s.name
strategies_full_name = s.full_name

play = True

while play:
    system("clear")
    # system("cls")
    print("**************************************************************")
    print("* 게임 모드를 선택하세요!                                    *")
    print("* 1: 상대 전략에 대응하는 최적의 수 찾기 (YOU vs COMPUTER)   *")
    print("* 2: 전략간 대결 시뮬레이션 (COMPUTER vs COMPUTER)           *")
    print("*    단판 시행                                               *")
    print("* 3: 전략간 대결 시뮬레이션 (COMPUTER vs COMPUTER)           *")
    print("*    ROUND 수를 1부터 늘려가며 시행                          *")
    print("* 0: 프로그램 종료                                           *")
    print("**************************************************************\n")
    mode = input("선택 >> ")

    if mode.isdigit():
        mode = int(mode)

    if mode == 0:
        print("종료합니다.")
        play = False
        continue

    elif mode == 1:
        match = int(input("총 ROUND수를 설정하세요. >> "))
        system("clear")
        # system("cls")
        log_tft("0: ")
        log_betray("1: ")
        log_coop("2: ")
        log_grudge("3: ")
        log_prober("4: ")
        strategy = int(input("상대방의 전략을 선택하세요. (0~4) >> "))
        select_strategy = strategies[strategy]
        system("clear")
        # system("cls")
        log_by_number(strategy, "상대방의 전략: ")
        log_credit()

        for i in range(match):
            scores = []
            for candidate in list(product(range(2), repeat=match)):
                score_board = [0] * 2
                minmax_calculate(
                    2,
                    match,
                    candidate,
                    select_strategy,
                    score_board,
                    PLAYER_ONE,
                    PLAYER_TWO,
                )
                scores.append(score_board[PLAYER_ONE])
            max_score = max(scores)
            min_score = min(scores)

        score_board = [0] * 2
        is_log = True
        battle(
            2,
            match,
            s.player,
            select_strategy,
            score_board,
            PLAYER_ONE,
            PLAYER_TWO,
            is_log,
            strategy
        )

        print(f"내 점수: {score_board[0]}")
        print(f"얻을 수 있었던 최대 점수: {max_score}")
        print(f"얻을 수 있었던 최소 점수: {min_score}")
        print()

    elif mode == 2:
        is_log = False
        round_num = input("몇 라운드 간 진행할까요? (R: 랜덤) ")
        if round_num == "R" or round_num == "r":
            round_num = str(randrange(1, 100000))

        if not round_num.isdigit():
            print("잘못 입력하셨습니다.")
            print()
        else:
            round_num = int(round_num)

        winning = [0] * len(strategies)
        total_score = [0] * len(strategies)

        for i in range(len(strategies) - 1):
            for j in range(i + 1, len(strategies)):
                score_board = [0] * 2
                battle(
                    3,
                    round_num,
                    strategies[i],
                    strategies[j],
                    score_board,
                    0,
                    1,
                    is_log,
                    0
                )
                if score_board[0] > score_board[1]:
                    winning[strategies.index(strategies[i])] += 1
                total_score[strategies.index(strategies[i])] += score_board[0]
                total_score[strategies.index(strategies[j])] += score_board[1]

        print()
        print(f"ROUND {round_num}")
        for i in range(len(total_score)):
            print(f"{total_score[i]}\t{strategies_full_name[i]}")
        print(
            f"최종 점수가 가장 높은 전략: {strategies_full_name[total_score.index(max(total_score))]}"
        )
        print()

    elif mode == 3:
        is_log = False
        end_round = int(input("몇 라운드까지 진행할까요? >> "))
        for round_num in range(1, end_round+1):

            winning = [0] * len(strategies)
            total_score = [0] * len(strategies)

            for i in range(len(strategies) - 1):
                for j in range(i + 1, len(strategies)):
                    score_board = [0] * 2
                    battle(
                        3,
                        round_num,
                        strategies[i],
                        strategies[j],
                        score_board,
                        0,
                        1,
                        is_log,
                        0
                    )
                    if score_board[0] > score_board[1]:
                        winning[strategies.index(strategies[i])] += 1
                    total_score[strategies.index(strategies[i])] += score_board[0]
                    total_score[strategies.index(strategies[j])] += score_board[1]

            system("clear")
            # system("cls")
            print(f"ROUND {round_num}")
            for i in range(len(total_score)):
                print(f"{total_score[i]}\t{strategies_full_name[i]}")
            print(
                f"최종 점수가 가장 높은 전략: {strategies_full_name[total_score.index(max(total_score))]}"
            )
            print()

    else:
        print("잘못 입력하셨습니다.")
        print()

    input("Press Enter to continue... ")
