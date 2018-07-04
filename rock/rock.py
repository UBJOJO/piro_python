# intro
# 가위바위보 메소드 => if 조건문
# 승 무 패 저장 -> dict

import random

intro_str = """
반가워요~
"""
input_msg = '1. 가위 2. 바위 3. 보, (종료 :Q, q)'
score_msg = "승 :{win}, 패 :{lost} 비김 :{draw}"

score = {'win': 0, 'draw': 0, 'lost': 0}
rep_set = ["가위", "바위", "보"]

while True:
    print(intro_str)
    while True:
        input_str = input(input_msg)
        if input_str in ['1', '2', '3', 'q', 'Q']:
            if input_str in ['q', 'Q']:
                break
            else:
                user = int(input_str)
                com = random.randint(1, 3)

                if user == com:
                    print("비겼습니다.")
                    score['draw'] += 1
                elif user % 3 + 1 == com:
                    print("졌습니다.")
                    score['lost'] += 1
                elif com % 3 + 1 == user:
                    print("이겼습니다.")
                    score['win'] += 1
                print(score_msg.format(
                    win = score['win'],
                    draw = score['draw'],
                    lost = score['lost']
                ))
        else:
            print("잘못골랐습니다. 다시골라주세요")

