"""
logging.py
* 화면에 출력할 각종 로그 함수들 모음
"""

# Tit-for-Tat 전략에 대한 설명 로깅
# @param msg: 같이 출력할 메시지
def log_tft(msg: str) -> None:
    print(f"{msg}Tit-for-Tat")
    print("- 처음엔 항상 협력합니다.\n- 이후에는 상대방이 이전에 했던 판단을 똑같이 따라합니다.\n")


# 난세 전략에 대한 설명 로깅
# @param msg: 같이 출력할 메시지
def log_betray(msg: str) -> None:
    print(f"{msg}난세")
    print("- 상대방의 선택과 상관없이 항상 배반합니다.\n")


# 황금률 전략에 대한 설명 로깅
# @param msg: 같이 출력할 메시지
def log_coop(msg: str) -> None:
    print(f"{msg}황금률")
    print("- 상대방의 선택과 상관없이 항상 협력합니다.\n")


# FriedMan 전략에 대한 설명 로깅
# @param msg: 같이 출력할 메시지
def log_grudge(msg: str) -> None:
    print(f"{msg}FriedMan (Grudger)")
    print("- 처음부터 계속 협력합니다.\n- 만약 상대가 한번이라도 배반을 했다면, 이후에는 계속해서 배반합니다.\n")


# Prober 전략에 대한 설명 로깅
# @param msg: 같이 출력할 메시지
def log_prober(msg: str) -> None:
    print(f"{msg}Prober")
    print(
        "- 1~4 라운드에서 협력-배반-협력-협력을 선택합니다.\n- 그 사이에 상대방이 한 번도 배반하지 않았다면 이후에는 계속해서 배반합니다.\n- 그렇지 않다면, Tit-for-Tat 전략을 사용합니다.\n"
    )


# 반복문 사용을 위한 함수배열
strategies_info = [log_tft, log_betray, log_coop, log_grudge, log_prober]

# 모든 전략을 로깅
def log_all_strategy() -> None:
    for i in range(len(strategies_info)):
        strategies_info[i](f"{i}: ")


# index에 맞는 전략을 로깅
# @param index: 전략이 strategies_info에서 위치한 index
# @param msg: 같이 출력할 메시지
def log_by_index(index: int, msg: str) -> None:
    strategies_info[index](msg)


# 점수표를 로깅
def log_credit() -> None:
    print("A\tB\tA점수\tB점수")
    print("협력\t협력\t+2\t+2")
    print("협력\t배반\t-1\t+3")
    print("배반\t협력\t+3\t-1")
    print("배반\t배반\t0\t0\n")


# 메인화면 선택지를 로깅
def log_title() -> None:
    print("**************************************************************")
    print("* 게임 모드를 선택하세요!                                    *")
    print("* 1: 상대 전략에 대응하는 최적의 수 찾기 (YOU vs COMPUTER)   *")
    print("* 2: 전략간 대결 시뮬레이션 (COMPUTER vs COMPUTER)           *")
    print("*    단판 시행                                               *")
    print("* 3: 전략간 대결 시뮬레이션 (COMPUTER vs COMPUTER)           *")
    print("*    ROUND 수를 1부터 늘려가며 시행                          *")
    print("* 0: 프로그램 종료                                           *")
    print("**************************************************************\n")
