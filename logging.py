def log_tft(msg):
    print(f"{msg}Tit-for-Tat")
    print("- 처음엔 항상 협력합니다.\n- 이후에는 상대방이 이전에 했던 판단을 똑같이 따라합니다.\n")

def log_betray(msg):
    print(f"{msg}난세")
    print("- 상대방의 선택과 상관없이 항상 배반합니다.\n")

def log_coop(msg):
    print(f"{msg}황금률")
    print("- 상대방의 선택과 상관없이 항상 협력합니다.\n")

def log_grudge(msg):
    print(f"{msg}FriedMan (Grudger)")
    print("- 처음부터 계속 협력합니다.\n- 만약 상대가 한번이라도 배반을 했다면, 이후에는 계속해서 배반합니다.\n")

def log_prober(msg):
    print(f"{msg}Prober")
    print("- 1~4 라운드에서 협력-배반-협력-협력을 선택합니다.\n- 그 사이에 상대방이 한 번도 배반하지 않았다면 이후에는 계속해서 배반합니다.\n- 그렇지 않다면, Tit-for-Tat 전략을 사용합니다.\n")

def log_by_number(number, msg):
    if number == 0:
        log_tft(msg)
    elif number == 1:
        log_betray(msg)
    elif number == 2:
        log_coop(msg)
    elif number == 3:
        log_grudge(msg)
    elif number == 4:
        log_prober(msg)

def log_credit():
    print("A\tB\tA점수\tB점수")
    print("협력\t협력\t+2\t+2")
    print("협력\t배반\t-1\t+3")
    print("배반\t협력\t+3\t-1")
    print("배반\t배반\t0\t0\n")