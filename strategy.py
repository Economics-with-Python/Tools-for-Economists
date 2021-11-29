import random


class Strategy:
    def __init__(self):
        self.COOPERATE = 1  # 협력
        self.BETRAY = 0  # 배반
        self.strategies = [
            self.ticfortat,
            self.always_betray,
            self.always_cooperate,
            self.grudge,
            self.prober,
            self.joss,
            self.random_select,
        ]

    def ticfortat(self, match, is_betrayed, previous_player_select):
        if match == 1:
            return self.COOPERATE
        return previous_player_select

    def always_betray(self, match, is_betrayed, previous_player_select):
        return self.BETRAY

    def always_cooperate(self, match, is_betrayed, previous_player_select):
        return self.COOPERATE

    def grudge(self, match, is_betrayed, previous_player_select):
        if match == 1:
            return self.COOPERATE
        if is_betrayed:
            return self.BETRAY
        return self.COOPERATE

    def prober(self, match, is_betrayed, previous_player_select):
        if match == 1 or match == 3 or match == 4:
            return self.COOPERATE
        elif match == 2:
            return self.BETRAY
        else:  # 5라운드 이후
            if is_betrayed:
                return self.ticfortat(match, is_betrayed, previous_player_select)
            else:
                return self.BETRAY

    def joss(self, match, is_betrayed, previous_player_select):
        if random.randrange(1, 11) == 1:
            return self.BETRAY
        return self.ticfortat(match, is_betrayed, previous_player_select)

    def random_select(self, match, is_betrayed, previous_player_select):
        return random.randrange(2)

    def player(self, match, is_betrayed, previous_player_select):
        return int(input("배반: 0, 협력: 1 >> "))
