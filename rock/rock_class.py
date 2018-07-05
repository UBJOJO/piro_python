import random

class game():
    intro_msg = "가위 바위 보 게임!! 안녕"
    input_msg = "1. 가위 2. 바위 3. 보 종료(q , Q)"
    choice_list = ('가위', '바위', '보')
    print_confirm_msg = "{user}를 내셨군요. 저는 {com}을 냈습니다."
    user = None
    com = None
    result = None

    def start(self):
        while True:
            self.intro()
            self.user = self.get_user_input()
            self.com = random.randint(1, 3)
            self.calc_result()
            self.print_confirm_msg()

    def intro(self):
         print(self.intro_msg)

    def get_user_input(self):
            while True:
                input_str = input(self.input_msg)
                if input_str in ['1', '2', '3', 'q', 'Q']:
                    if input_str in ['q', 'Q']:
                        print("dkssudgl rktpdy")
                        exit()
                    else:
                        return int(input_str)
                        user = int(input_str)
                        break
                else:
                    print("잘못골랐어요 다시")
            return user

    def cal_result(self):
        if self.user == self.com:
            self.result = "draw"
        elif self.user % 3 + 1 == self.com:
            self.result = "lost"
        elif self.com % 3 + 1 == self.user:
            self.result = "win"
        return result


rock = game()
rock.start()



# class game():
#     intro_msg = '1. 가위, 2. 바위, 3. 보, (종료 :Q, q)''
#
#
#     input_msg = '1. 가위, 2. 바위, 3. 보, (종료 :Q, q)'
#     while True:
#         input_str = input(input_msg)
#         if input_str in ['1', '2', '3', 'q', 'Q']:
#             if input_str in ['q', 'Q']:
#                 exit()
#             else:
#                 user = int(input_str)
#                 break
#         else:
#             print("잘못골랐어요 다시")
#     return user

# def calc_result(user, com):
#     if user == com:
#         result = "draw"
#     elif user % 3 + 1 == com:
#         result = "lost"
#     elif com % 3 + 1 == user:
#         result = "win"
#     return result