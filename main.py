ROUND = 5
player_score = 0
com_score = 0  # tic for tac

PLAYER = 0
COM = 1

COOPERATE = 1  # 협력
BETRAY = 0  # 배반
BOARD = [[[0, 0], [3, -1]], [[-1, 3], [2, 2]]]


def ticfortat(round, previous_player_select):
    if round == 1:
        return COOPERATE
    return previous_player_select


def always_betray():
    return BETRAY


def always_cooperate():
    return COOPERATE


def grudge(round, is_betrayed):
    if round == 1:
        return COOPERATE
    if is_betrayed:
        return BETRAY
    return COOPERATE


def prober(round, is_betrayed, previous_player_select):
    if round == 1 or round == 3 or round == 4:
        return COOPERATE
    elif round == 2:
        return BETRAY
    else:  # 5라운드 이후
        if is_betrayed:
            return ticfortat(round, previous_player_select)
        else:
            return BETRAY


def calculate(player_select, com_select):
    global player_score, com_score
    player_score += BOARD[player_select][com_select][PLAYER]
    com_score += BOARD[player_select][com_select][COM]


def calculate_com(p1_select, p2_select, p1_index, p2_index):
    global score_board
    score_board[p1_index] += BOARD[p1_select][p2_select][0]
    score_board[p2_index] += BOARD[p1_select][p2_select][1]


"""
previous_player_select = None
is_betrayed = False
for i in range(1, ROUND + 1):
    player_select = int(input("배반: 0, 협력: 1 >> "))
    com_select = ticfortat(i, previous_player_select)
    calculate(player_select, com_select)
    if player_select == BETRAY:
        is_betrayed = True
    previous_player_select = player_select
    print(f"ticfortat/{i}round # player score: {player_score}")

ROUND = 4
previous_player_select = None
is_betrayed = False
for i in range(1, ROUND + 1):
    player_select = int(input("배반: 0, 협력: 1 >> "))
    com_select = always_betray()
    calculate(player_select, com_select)
    if player_select == BETRAY:
        is_betrayed = True
    previous_player_select = player_select
    print(f"always_bet/{i}round # player score: {player_score}")

ROUND = 4
previous_player_select = None
is_betrayed = False
for i in range(1, ROUND + 1):
    player_select = int(input("배반: 0, 협력: 1 >> "))
    com_select = always_cooperate()
    calculate(player_select, com_select)
    if player_select == BETRAY:
        is_betrayed = True
    previous_player_select = player_select
    print(f"always_coop/{i}round # player score: {player_score}")

ROUND = 5
previous_player_select = None
is_betrayed = False
for i in range(1, ROUND + 1):
    player_select = int(input("배반: 0, 협력: 1 >> "))
    com_select = grudge(i, is_betrayed)
    calculate(player_select, com_select)
    if player_select == BETRAY:
        is_betrayed = True
    previous_player_select = player_select
    print(f"grudge/{i}round # player score: {player_score}")

ROUND = 7
previous_player_select = None
is_betrayed = False
for i in range(1, ROUND + 1):
    player_select = int(input("배반: 0, 협력: 1 >> "))
    com_select = prober(i, is_betrayed, previous_player_select)
    calculate(player_select, com_select)
    if player_select == BETRAY:
        is_betrayed = True
    previous_player_select = player_select
    print(f"prober/{i}round # player score: {player_score}")

print()
print("***** 경기 종료 *****")
print(f"PLAYER: {player_score}점")
print(f"COMPUTER: {com_score}점")

"""

###################### 2번째 게임


# 0:tft 1:always_bet 2:always_coop 3:grudge 4:prober
score_board = [0] * 5
STRATEGY = ["Tic for Tat", "Always Betray", "Always Cooperate", "Grudge", "Prober"]

# tft(0) vs always_bet(1)
ROUND = 10
p1_previous = None
p1_is_betrayed = False
p2_previous = None
p2_is_betrayed = False
for i in range(1, ROUND + 1):
    p1_select = ticfortat(i, p2_previous)
    p2_select = always_betray()
    calculate_com(p1_select, p2_select, 0, 1)
    if p1_select == BETRAY:
        p1_is_betrayed = True
    if p2_select == BETRAY:
        p2_is_betrayed = True
    p1_previous = p1_select
    p2_previous = p2_select


# tft(0) vs always_coop(2)
ROUND = 10
p1_previous = None
p1_is_betrayed = False
p2_previous = None
p2_is_betrayed = False
for i in range(1, ROUND + 1):
    p1_select = ticfortat(i, p2_previous)
    p2_select = always_cooperate()
    calculate_com(p1_select, p2_select, 0, 2)
    if p1_select == BETRAY:
        p1_is_betrayed = True
    if p2_select == BETRAY:
        p2_is_betrayed = True
    p1_previous = p1_select
    p2_previous = p2_select


# tft(0) vs grudge(3)
ROUND = 10
p1_previous = None
p1_is_betrayed = False
p2_previous = None
p2_is_betrayed = False
for i in range(1, ROUND + 1):
    p1_select = ticfortat(i, p2_previous)
    p2_select = grudge(i, p1_is_betrayed)
    calculate_com(p1_select, p2_select, 0, 3)
    if p1_select == BETRAY:
        p1_is_betrayed = True
    if p2_select == BETRAY:
        p2_is_betrayed = True
    p1_previous = p1_select
    p2_previous = p2_select


# tft(0) vs prober(4)
ROUND = 10
p1_previous = None
p1_is_betrayed = False
p2_previous = None
p2_is_betrayed = False
for i in range(1, ROUND + 1):
    p1_select = ticfortat(i, p2_previous)
    p2_select = prober(i, p1_is_betrayed, p1_previous)
    calculate_com(p1_select, p2_select, 0, 4)
    if p1_select == BETRAY:
        p1_is_betrayed = True
    if p2_select == BETRAY:
        p2_is_betrayed = True
    p1_previous = p1_select
    p2_previous = p2_select


# always_bet(1) vs always_coop(2)
ROUND = 10
p1_previous = None
p1_is_betrayed = False
p2_previous = None
p2_is_betrayed = False
for i in range(1, ROUND + 1):
    p1_select = always_betray()
    p2_select = always_cooperate()
    calculate_com(p1_select, p2_select, 1, 2)
    if p1_select == BETRAY:
        p1_is_betrayed = True
    if p2_select == BETRAY:
        p2_is_betrayed = True
    p1_previous = p1_select
    p2_previous = p2_select


# always_bet(1) vs grudge(3)
ROUND = 10
p1_previous = None
p1_is_betrayed = False
p2_previous = None
p2_is_betrayed = False
for i in range(1, ROUND + 1):
    p1_select = always_betray()
    p2_select = grudge(i, p1_is_betrayed)
    calculate_com(p1_select, p2_select, 1, 3)
    if p1_select == BETRAY:
        p1_is_betrayed = True
    if p2_select == BETRAY:
        p2_is_betrayed = True
    p1_previous = p1_select
    p2_previous = p2_select


# always_bet(1) vs prober(4)
ROUND = 10
p1_previous = None
p1_is_betrayed = False
p2_previous = None
p2_is_betrayed = False
for i in range(1, ROUND + 1):
    p1_select = always_betray()
    p2_select = prober(i, p1_is_betrayed, p1_previous)
    calculate_com(p1_select, p2_select, 1, 4)
    if p1_select == BETRAY:
        p1_is_betrayed = True
    if p2_select == BETRAY:
        p2_is_betrayed = True
    p1_previous = p1_select
    p2_previous = p2_select


# always_coop(2) vs grudge(3)
ROUND = 10
p1_previous = None
p1_is_betrayed = False
p2_previous = None
p2_is_betrayed = False
for i in range(1, ROUND + 1):
    p1_select = always_cooperate()
    p2_select = grudge(i, p1_is_betrayed)
    calculate_com(p1_select, p2_select, 2, 3)
    if p1_select == BETRAY:
        p1_is_betrayed = True
    if p2_select == BETRAY:
        p2_is_betrayed = True
    p1_previous = p1_select
    p2_previous = p2_select


# always_coop(2) vs prober(4)
ROUND = 10
p1_previous = None
p1_is_betrayed = False
p2_previous = None
p2_is_betrayed = False
for i in range(1, ROUND + 1):
    p1_select = always_cooperate()
    p2_select = prober(i, p1_is_betrayed, p1_previous)
    calculate_com(p1_select, p2_select, 2, 4)
    if p1_select == BETRAY:
        p1_is_betrayed = True
    if p2_select == BETRAY:
        p2_is_betrayed = True
    p1_previous = p1_select
    p2_previous = p2_select


# grudge(3) vs prober(4)
ROUND = 10
p1_previous = None
p1_is_betrayed = False
p2_previous = None
p2_is_betrayed = False
for i in range(1, ROUND + 1):
    p1_select = grudge(i, p2_is_betrayed)
    p2_select = prober(i, p1_is_betrayed, p1_previous)
    calculate_com(p1_select, p2_select, 3, 4)
    if p1_select == BETRAY:
        p1_is_betrayed = True
    if p2_select == BETRAY:
        p2_is_betrayed = True
    p1_previous = p1_select
    p2_previous = p2_select

for i in range(5):
    print(f"{STRATEGY[i]}: {score_board[i]}")
print(f"우승: {STRATEGY[score_board.index(max(score_board))]}")
