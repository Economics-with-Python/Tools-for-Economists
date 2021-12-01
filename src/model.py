"""
model.py
* 각종 연산을 수행
"""

from strategy import *

# 보상표
# 상호협력: +2, +2
# 상호배반: 0, 0
# 한쪽만 배반: +3(배반), -1(협력)
BOARD = [[[0, 0], [3, -1]], [[-1, 3], [2, 2]]]

PLAYER_ONE = 0
PLAYER_TWO = 1

BETRAY = 0  # 배반
COOPERATE = 1  # 협력


# 보상표에서 선택에 따른 결과 반환
# @param p1_select: player 1의 선택
# @param p2_select: player 2의 선택
# @return: 계산된 점수가 담긴 튜플 (player 1가 획득할 점수, player 2가 획득할 점수)
def calculate(p1_select: int, p2_select: int) -> list:
    p1_score = BOARD[p1_select][p2_select][PLAYER_ONE]
    p2_score = BOARD[p1_select][p2_select][PLAYER_TWO]
    return (p1_score, p2_score)


# 정해진 라운드 수 만큼 두 전략이 대결
# @param total_match: 수행할 라운드 수
# @param p1: player 1의 전략
# @param p2: player 2의 전략
# @param is_log: 라운드 마다 진행한 배틀의 로그를 출력할지 여부
def battle(total_match: int, p1: Strategy, p2: Strategy, is_log: bool) -> None:
    p1_is_betrayed = False
    p2_is_betrayed = False
    for i in range(1, total_match + 1):
        p1_select = p1.select()
        p2_select = p2.select()
        result = calculate(p1_select, p2_select)
        if p1_select == BETRAY:
            p1_is_betrayed = True
        if p2_select == BETRAY:
            p2_is_betrayed = True
        p1.update(p2_is_betrayed, p2_select, result[PLAYER_ONE])
        p2.update(p1_is_betrayed, p1_select, result[PLAYER_TWO])

        if is_log:
            battle_log(i, total_match, p1, p2)


# 사용자가 선택 가능한 수를 배열에 담아, 가상 매치업 점수 반환
# @param total_match: 수행할 라운드 수
# @param p1: player 1의 선택을 담은 리스트
#            ex - [0, 1, 1, 0, 1]
# @param p2: player 2의 전략
# @return: 배틀이 끝난 후 p1이 얻은 점수
def calculate_score(total_match: int, p1: list, p2: Strategy) -> int:
    score = 0
    p1_is_betrayed = False
    for i in range(1, total_match + 1):
        p1_select = p1[i - 1]
        p2_select = p2.select()
        result = calculate(p1_select, p2_select)
        score += result[PLAYER_ONE]
        if p1_select == BETRAY:
            p1_is_betrayed = True
        p2.update(p1_is_betrayed, p1_select, result[PLAYER_TWO])
    return score


# 로깅을 위해 int 형의 숫자를 str 형으로 변환
# @param select: player가 고른 선택 (0, 1)
# @return: str로 변환된 player의 선택 (0: "배반", 1: "협력")
def convert_select(select: int) -> str:
    if select == BETRAY:
        return "배반"
    return "협력"


# 단판에 대한 결과를 로깅
# @param match: 해당 판이 몇번째 라운드인지
# @param total_match: 총 몇라운드까지 진행하는지
# @p1: player1의 정보를 담고 있는 객체
# @p2: player2의 정보를 담고 있는 객체
def battle_log(match: int, total_match: int, p1: Strategy, p2: Strategy) -> None:
    print(f"\n{p1.name} vs {p2.name} # ROUND {match} of {total_match}")
    print(f"Player\tSelect\tGet\tScore")
    # player 1의 직전 선택에 대한 정보는 player 2의 previous에 담겨있음
    print(
        f"{p1.short_name}\t{convert_select(p2.previous)}\t{BOARD[p2.previous][p1.previous][PLAYER_ONE]}\t{p1.score}"
    )
    print(
        f"{p2.short_name}\t{convert_select(p1.previous)}\t{BOARD[p2.previous][p1.previous][PLAYER_TWO]}\t{p2.score}\n"
    )
