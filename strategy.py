import random
from os import system
from logging import *

class Strategy:
    def __init__(self):
        self.COOPERATE = 1  # 협력
        self.BETRAY = 0  # 배반
        self.strategies = [
            self.titfortat,
            self.always_betray,
            self.always_cooperate,
            self.grudge,
            self.prober,
            self.joss,
            self.random_select,
        ]
        self.name = [
            "TfT",
            "난세",
            "황금률",
            "FM",
            "Pb",
            "Joss",
            "Rand",
        ]
        self.full_name = [
            "Tit-for-Tat",
            "난세",
            "황금률",
            "FriedMan (Grudger)",
            "Prober",
            "Joss",
            "Random"
        ]
        self.strategy_index = [
            "titfortat",
            "always_betray",
            "always_cooperate",
            "grudge",
            "prober",
            "joss",
            "random_select"
        ]

    def titfortat(self, match, is_betrayed, previous_player_select, strategy_number, total_round):
        if match == 1:
            return self.COOPERATE
        return previous_player_select

    def always_betray(self, match, is_betrayed, previous_player_select, strategy_number, total_round):
        return self.BETRAY

    def always_cooperate(self, match, is_betrayed, previous_player_select, strategy_number, total_round):
        return self.COOPERATE

    def grudge(self, match, is_betrayed, previous_player_select, strategy_number, total_round):
        if match == 1:
            return self.COOPERATE
        if is_betrayed:
            return self.BETRAY
        return self.COOPERATE

    def prober(self, match, is_betrayed, previous_player_select, strategy_number, total_round):
        if match == 1 or match == 3 or match == 4:
            return self.COOPERATE
        elif match == 2:
            return self.BETRAY
        else:  # 5라운드 이후
            if is_betrayed:
                return self.titfortat(match, is_betrayed, previous_player_select, strategy_number, total_round)
            else:
                return self.BETRAY

    def joss(self, match, is_betrayed, previous_player_select, strategy_number, total_round):
        if random.randrange(1, 11) == 1:
            return self.BETRAY
        return self.titfortat(match, is_betrayed, previous_player_select, strategy_number, total_round)

    def random_select(self, match, is_betrayed, previous_player_select, strategy_number, total_round):
        return random.randrange(2)

    def player(self, match, is_betrayed, previous_player_select, strategy_number, total_round):
        ok = True
        while ok:
            select = input(f"TOTAL {total_round} ROUND\n# ROUND {match}\n배반: 0, 협력: 1 >> ")
            system("clear")
            log_by_number(strategy_number, "상대방의 전략: ")
            log_credit()
            if select != "0" and select != "1":
                print("잘못 입력하셨습니다.\n")
                continue
            return int(select)
