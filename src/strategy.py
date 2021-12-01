"""
strategy.py
* 게임이론에서 취할 수 있는 전략들을 정의해둔 파일
"""

from os import system
from logging import *
import random
import platform

# 콘솔창 초기화를 위한 운영체제 확인
if platform.system() == "Windows":
    CLEAR = "cls"
else:
    CLEAR = "clear"


# 가장 기본적인 Tit-for-Tat 전략
# @param previous: 상대방이 전에 취했던 전략
# @return: 상대방이 전에 취했던 전략
def basic_titfortat(previous: int) -> int:
    return previous


class Strategy:
    COOPERATE = 1
    BETRAY = 0
    current_round = 1  # 현재 라운드 정보를 담은 변수
    name = ""  # 전략의 full name
    short_name = ""  # 전략의 short name
    score = 0  # 전략의 현재 점수

    # 한 라운드가 진행되고, 필요한 정보들을 업데이트
    # @param is_betrayed: 상대방이 배신을 한 적이 있는지
    # @param previous: 상대방이 이전에 취한 선택
    # @param score: 나의 점수
    def update(self, is_betrayed: bool, previous: int, score: int) -> None:
        self.is_betrayed = is_betrayed
        self.previous = previous
        self.current_round += 1
        self.score += score

    # 전략별로 선택을 반환
    # @return: 선택 (배반: 0, 협력: 1)
    def select(self) -> int:
        return None


# Tit-for-Tat
# 첫 라운드에는 협력
# 이후에는 상대방이 직전에 했던 전략을 따라함
class Titfortat(Strategy):
    def __init__(self) -> None:
        self.name = "Tit-for-Tat"
        self.short_name = "TfT"

    def select(self) -> int:
        if self.current_round == 1:
            return self.COOPERATE
        return basic_titfortat(self.previous)


# 배반
# 무조건 배반
class AlwaysBetray(Strategy):
    def __init__(self) -> None:
        self.name = "난세"
        self.short_name = "난세"

    def select(self) -> int:
        return self.BETRAY


# 황금률
# 무조건 협력
class AlwaysCooperate(Strategy):
    def __init__(self) -> None:
        self.name = "황금률"
        self.short_name = "황금률"

    def select(self) -> int:
        return self.COOPERATE


# FriedMan (Grudger)
# 계속해서 협력
# 하지만 상대방이 한 번이라도 배신한 경우 끝까지 배신
class Grudge(Strategy):
    def __init__(self) -> None:
        self.name = "FriedMan (Grudger)"
        self.short_name = "FM"

    def select(self) -> int:
        if self.current_round == 1:
            return self.COOPERATE
        if self.is_betrayed:
            return self.BETRAY
        return self.COOPERATE


# Prober
# 첫 4라운드는 협력-배신-협력-협력의 순서로 진행
# 4라운드 사이에 상대방이 한 번도 배반하지 않았다면, 남은 라운드는 모두 배반
# 4라운드 사이에 상대방이 한 번이라도 배반했다면, 남은 라운드는 Tit-for-Tat 전략을 취함
class Prober(Strategy):
    def __init__(self) -> None:
        self.name = "Prober"
        self.short_name = "Pbr"

    def select(self) -> int:
        if (
            self.current_round == 1
            or self.current_round == 3
            or self.current_round == 4
        ):
            return self.COOPERATE
        elif self.current_round == 2:
            return self.BETRAY
        else:  # 5라운드 이후
            if self.is_betrayed:
                return basic_titfortat(self.previous)
            else:
                return self.BETRAY


# Joss
# Tit-for-Tat과 같은 전략을 취함
# 1/10의 확률로 선제 배반
class Joss(Strategy):
    def __init__(self) -> None:
        self.name = "Joss"
        self.short_name = "Joss"

    def select(self) -> int:
        if random.randrange(1, 11) == 1:
            return self.BETRAY
        if self.current_round == 1:
            return self.COOPERATE
        return basic_titfortat(self.previous)


# All Random
# 랜덤으로 협력, 배반
class AllRandom(Strategy):
    def __init__(self) -> None:
        self.name = "All Random"
        self.short_name = "AR"

    def select(self) -> int:
        return random.randrange(2)


# Player
# 사용자가 취하는 전략
# 0, 1을 입력받아 선택
class Player(Strategy):
    def __init__(self, computer_index) -> None:
        self.name = "YOU"
        self.short_name = "YOU"
        self.computer_index = computer_index

    def select(self) -> int:
        ok = True
        while ok:
            select = input(f"# ROUND {self.current_round}\n배반: 0, 협력: 1 >> ")

            system(CLEAR)
            log_by_index(self.computer_index, "상대방의 전략: ")
            log_credit()

            if select != "0" and select != "1":
                print("잘못 입력하셨습니다.\n")
                continue
            return int(select)
