from strategy import Strategy


BOARD = [[[0, 0], [3, -1]], [[-1, 3], [2, 2]]]
PLAYER_ONE = 0
PLAYER_TWO = 1

s = Strategy()
strategies = s.strategies
strategies_name = s.name
strategies_index = s.strategy_index



def calculate(p1_select, p2_select):
    p1_score = BOARD[p1_select][p2_select][PLAYER_ONE]
    p2_score = BOARD[p1_select][p2_select][PLAYER_TWO]
    return (p1_score, p2_score)


def battle(
    mode, round, p1_strategy, p2_strategy, score_board, p1_index, p2_index, is_log, strategy_number
):
    p1_previous = None
    p2_previous = None
    p1_is_betrayed = False
    p2_is_betrayed = False
    for i in range(1, round + 1):
        p1_select = p1_strategy(i, p2_is_betrayed, p2_previous, strategy_number, round)
        p2_select = p2_strategy(i, p1_is_betrayed, p1_previous, strategy_number, round)
        calculated_score = calculate(p1_select, p2_select)
        score_board[p1_index] += calculated_score[PLAYER_ONE]
        score_board[p2_index] += calculated_score[PLAYER_TWO]
        if p1_select == s.BETRAY:
            p1_is_betrayed = True
        if p2_select == s.BETRAY:
            p2_is_betrayed = True
        p1_previous = p1_select
        p2_previous = p2_select
        if is_log:
            battle_log(
                mode,
                i,
                "YOU",
                strategies_name[strategies_index.index(p2_strategy.__name__)],
                p1_select,
                p2_select,
                score_board[p1_index],
                score_board[p2_index],
            )


def minmax_calculate(mode, round, p1, p2_strategy, score_board, p1_index, p2_index):
    p1_previous = None
    p2_previous = None
    p1_is_betrayed = False
    p2_is_betrayed = False
    for i in range(1, round + 1):
        p1_select = p1[i - 1]
        p2_select = p2_strategy(i, p1_is_betrayed, p1_previous, 0, round)
        calculated_score = calculate(p1_select, p2_select)
        score_board[p1_index] += calculated_score[PLAYER_ONE]
        score_board[p2_index] += calculated_score[PLAYER_TWO]
        if p1_select == s.BETRAY:
            p1_is_betrayed = True
        if p2_select == s.BETRAY:
            p2_is_betrayed = True
        p1_previous = p1_select
        p2_previous = p2_select


def convert_select(select):
    if select == s.BETRAY:
        return "배반"
    return "협력"


def battle_log(
    mode,
    round,
    p1_strategy_name,
    p2_strategy_name,
    p1_select,
    p2_select,
    p1_score,
    p2_score,
):
    if mode == 1:
        p2_strategy_name = "Anonym"
        p2_score = "-"
    print()
    print(f"{p1_strategy_name} vs {p2_strategy_name} # ROUND {round}")
    print(f"Player\tSelect\tGet\tScore")
    print(
        f"{p1_strategy_name}\t{convert_select(p1_select)}\t{BOARD[p1_select][p2_select][PLAYER_ONE]}\t{p1_score}"
    )
    print(
        f"{p2_strategy_name}\t{convert_select(p2_select)}\t{BOARD[p1_select][p2_select][PLAYER_TWO]}\t{p2_score}"
    )
    print()
