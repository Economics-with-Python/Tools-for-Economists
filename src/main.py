"""
main.py
* 프로젝트 메인 파일
* 한양대학교 ERICA Economics with Python 참가작
* 2021.11.30
"""

from itertools import product
from random import randrange
from os import system
import platform
from logging import *
from strategy import *
from model import *

# 콘솔창 초기화를 위한 운영체제 확인
if platform.system() == "Windows":
    CLEAR = "cls"
else:
    CLEAR = "clear"

play = True
while play:
    system(CLEAR)
    log_title()
    mode = input("선택 >> ")

    if mode.isdigit():
        mode = int(mode)

    # mode 0: 종료
    if mode == 0:
        print("종료합니다.")
        play = False

    # mode 1: YOU vs COM - 최적의 수 찾기
    elif mode == 1:
        while True:
            total_match = input("총 ROUND수를 설정하세요. (30이하) >> ")
            if total_match.isdigit() and (1 <= int(total_match) <= 30):
                total_match = int(total_match)
                break
            print("잘못 입력하셨습니다.\n")

        system(CLEAR)
        log_all_strategy()

        while True:
            index = input("상대방의 전략을 선택하세요. (0~4) >> ")
            if index.isdigit() and (0 <= int(index) <= 4):
                index = int(index)
                break
            print("잘못 입력하셨습니다.\n")

        strategies = [Titfortat, AlwaysBetray, AlwaysCooperate, Grudge, Prober]
        select_strategy = strategies[index]

        system(CLEAR)
        log_by_index(index, "상대방의 전략: ")
        log_credit()
        print(f"TOTAL {total_match} ROUND")

        # 가능한 최대점과 최소점 계산
        computer = select_strategy()
        for i in range(total_match):
            scores = []
            for candidate in list(product(range(2), repeat=total_match)):
                scores.append(calculate_score(total_match, candidate, computer))
        max_score = max(scores)
        min_score = min(scores)

        # YOU vs COM
        is_log = True
        player = Player(index)
        computer = select_strategy()
        battle(total_match, player, computer, is_log)

        print(f"내 점수: {player.score}")
        print(f"얻을 수 있었던 최대 점수: {max_score}")
        print(f"얻을 수 있었던 최소 점수: {min_score}\n")

    # mode 2: COM vs COM - 단판 시행
    elif mode == 2:
        while True:
            total_match = input("몇 라운드 간 진행할까요? (R: 랜덤, 100000 이하) >> ")
            if total_match in ("R", "r"):
                total_match = randrange(1, 100000)
                break

            if total_match.isdigit() and (1 <= int(total_match) <= 100000):
                total_match = int(total_match)
                break

            print("잘못 입력하셨습니다.\n")

        strategies = [
            Titfortat,
            AlwaysBetray,
            AlwaysCooperate,
            Grudge,
            Prober,
            Joss,
            AllRandom,
        ]
        total_score = [0] * len(strategies)

        # COM vs COM - 매 경기 전략별로 획득한 score를 total_score 리스트에 누적
        is_log = False
        for i in range(len(strategies) - 1):
            for j in range(i + 1, len(strategies)):
                p1 = strategies[i]()
                p2 = strategies[j]()
                battle(total_match, p1, p2, is_log)
                total_score[i] += p1.score
                total_score[j] += p2.score

        print(f"\nROUND {total_match}")
        for i in range(len(total_score)):
            print(f"{total_score[i]}\t{strategies[i]().name}")
        print(
            f"최종 점수가 가장 높은 전략: {strategies[total_score.index(max(total_score))]().name}"
        )
        print()

    # mode 3: COM vs COM - 라운드를 늘려가며 반복 시행
    elif mode == 3:
        while True:
            end_round = input("몇 라운드까지 진행할까요? (2000 이하) >> ")
            if end_round.isdigit() and (1 <= int(end_round) <= 2000):
                end_round = int(end_round)
                break
            print("잘못 입력하셨습니다.\n")

        # COM vs COM - 콘솔창을 계속 초기화해, 같은 자리에서 업데이트 되는 것 처럼 보이도록 구성
        is_log = False
        for total_match in range(1, end_round + 1):
            strategies = [
                Titfortat,
                AlwaysBetray,
                AlwaysCooperate,
                Grudge,
                Prober,
                Joss,
                AllRandom,
            ]
            total_score = [0] * len(strategies)

            for i in range(len(strategies) - 1):
                for j in range(i + 1, len(strategies)):
                    p1 = strategies[i]()
                    p2 = strategies[j]()
                    battle(total_match, p1, p2, is_log)
                    total_score[i] += p1.score
                    total_score[j] += p2.score

            system(CLEAR)

            print(f"ROUND {total_match}")
            for i in range(len(total_score)):
                print(f"{total_score[i]}\t{strategies[i]().name}")
            print(
                f"최종 점수가 가장 높은 전략: {strategies[total_score.index(max(total_score))]().name}"
            )
            print()

    else:
        print("잘못 입력하셨습니다.\n")

    input("Press Enter to continue... ")
