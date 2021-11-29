from itertools import product
from strategy import Strategy
from util import *

strategies = Strategy().strategies

play = True

while play:
    print("**************************************************************")
    print("* 게임 모드를 선택하세요!                                    *")
    print("* 1: 상대 전략에 대응하는 최적의 수 찾기 (YOU vs COMPUTER)   *")
    print("* 2: 전략들 승률 분석 (COMPUTER vs COMPUTER)                 *")
    print("* 0: 프로그램 종료                                           *")
    print("**************************************************************\n")
    mode = int(input("선택: "))

    if mode == 0:
        play = False
        continue

    elif mode == 1:
        match = int(input("round 수를 설정하세요. "))
        strategy = int(input("상대방의 전략을 선택하세요. 0~5 "))
        select_strategy = strategies[strategy]
        print(f"상대방의 전략: {select_strategy.__name__}")
        print()

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
            strategy_class.player,
            select_strategy,
            score_board,
            PLAYER_ONE,
            PLAYER_TWO,
            is_log,
        )

        print(f"내 점수: {score_board[0]}")
        print(f"얻을 수 있었던 최대 점수: {max_score}")
        print(f"얻을 수 있었던 최소 점수: {min_score}")
        print()

    elif mode == 2:
        is_log = False
        round_num = int(input("몇 라운드 간 진행할까요?"))

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
                )
                if score_board[0] > score_board[1]:
                    winning[strategies.index(strategies[i])] += 1
                total_score[strategies.index(strategies[i])] += score_board[0]
                total_score[strategies.index(strategies[j])] += score_board[1]

        print(winning)
        print(total_score)
        print(
            f"가장 승률이 가장 높은 전략: {strategies[winning.index(max(winning))].__name__.capitalize()}"
        )
        print(
            f"최종 점수가 가장 높은 전략: {strategies[total_score.index(max(total_score))].__name__.capitalize()}"
        )
        print()

    else:
        print("잘못 입력하셨습니다.")
        print()
